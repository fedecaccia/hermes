import definitions

import datetime

import numpy as np

from algorithm import Algorithm


class StatArb(Algorithm):

    def __init__(self, algo_id, algo_values, data_modules, assets, oracle, world):

        """
        + Description: Statistical arbitrage constructor.
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: Array of all data modules objects. Super only saves what here cares.
        - assets: Dictionary of all assets objetcs. Super only saves what here cares.
        - oracle: Oracle object.
        - world: World object.
        + Output:
        -
        """
        
        super().__init__(algo_id, algo_values, data_modules, assets, oracle)
        self._world = world
        self._initialize_variables()

    def _check_data_modules(self):

        """
        + Description: check that data module received is right.
        + Input:
        -
        + Output:
        -
        """
        
        self._check_data_modules_amount()
        self._check_data_modules_description()
        self._check_data_modules_source()
        self._check_data_type()

    def _check_data_modules_amount(self):

        """
        + Description: check that amonut data modules received is right.
        + Input:
        -
        + Output:
        -
        """

        if len(self.data_modules)!=2:
            raise ValueError("Error using: "+str(len(self.data_modules))+" data modules in algorithm with id: '"
                             +str(self.id)+"'. You can only use 2.")

    def _check_data_modules_description(self):

        """
        + Description: check that data modules description received is right.
        + Input:
        -
        + Output:
        -
        """

        for module in self.data_modules:
            if module.description not in definitions.all_tickers:
                raise ValueError("Bad description in data module id: "
                +str(module.id))

    def _check_data_modules_source(self):

        """
        + Description: check that data modules source received is right.
        + Input:
        -
        + Output:
        -
        """

        for module in self.data_modules:
            if module.source not in definitions.all_exchanges:
                raise ValueError("Bad source in data module id: "
                +str(module.id))

    def _check_data_type(self):

        """
        + Description: check that data type in modules received is right.
        + Input:
        -
        + Output:
        -
        """

        for module in self.data_modules:
            if module.data_type != definitions.orderbook:
                raise ValueError("Bad data type in data module id: "
               +str(module.id)
                +". Expected: "+definitions.orderbook)

    def _check_parameters(self, algo_values):

        """
        + Description: Check parameters received in algo_values dictionary.
        + Input:
        - algo values: Dictionary containing algorithmic parameters defined in config.py.
        + Output:
        -
        """

        algo_params = algo_values[definitions.algo_params]
        
        try:
            self._limit_buy_pct = algo_params[definitions.limit_buy_pct]
        except:
            raise ValueError("Error trying to parse limit_buy_pct in algorithm: '"+self.id+"' parameters.")
                
        try:
            self._limit_sell_pct = algo_params[definitions.limit_sell_pct]
        except:
            raise ValueError("Error trying to parse limit_sell_pct in algorithm: '"+self.id+"' parameters.")
        

        try:
            self._max_delay_in_data = datetime.timedelta(seconds=algo_params[definitions.max_delay_in_data])
        except:
            raise ValueError("Error trying to parse max_delay_in_data in algorithm: '"+self.id+"' parameters.")
        
        try:
            self._usd_amount_to_trade = algo_params[definitions.usd_amount_to_trade]
        except:
            raise ValueError("Error trying to parse usd_amount_to_trade in algorithm: '"+self.id+"' parameters.")
        
        try:
            self._period = algo_params[definitions.period]
        except:
            raise ValueError("Error trying to parse period in algorithm: '"+self.id+"' parameters.")
        
        try:
            self._min_usd_profit = algo_params[definitions.min_usd_profit]
        except:
            raise ValueError("Error trying to parse period in algorithm: '"+self.id+"' parameters.")

    def _initialize_variables(self):
        
        """
        + Description: Initialize useful variables.
        + Input:
        -
        + Output:
        -
        """

        self.p_l0_s1 = np.array(())
        self.p_l1_s0 = np.array(())
        self.required_status = {
            definitions.long_position: None,
            definitions.short_position: None
        }
        self.status = {
            definitions.long_position: None,
            definitions.short_position: None
        }
        # store to compare next round
        self.time0_prev = datetime.datetime(2000, 1, 1, 0, 0)
        self.time1_prev = datetime.datetime(2000, 1, 1, 0, 0)
        self.prev_profit = 0
        self.prev_amount = 0

    def get_weight_val(self, row, side, amount):

        """
        + Description: Get a weighted value.
        + Input:
        - row:
        - side:
        - amount:
        + Output:
        - price:
        - params: Dictionary of order parameters.
        """
    
        count = 0
        price = 0

        if side=="ask":     

            price = row["ask_val_0"]
            count = row["ask_count_0"]        
            if count < amount:
                more_orders = row["ask_count_1"]
                if count+more_orders<=amount:
                    new_count = more_orders
                else:
                    new_count = amount-count
                price = (price * count + row["ask_val_1"]*new_count ) / (count+new_count)
                count += new_count

                if count < amount:
                    more_orders = row["ask_count_2"]
                    if count+more_orders>=amount:
                        new_count = amount-count
                        price = (price * count + row["ask_val_2"]*new_count ) / (count+new_count)
                    else:
                        price = row["ask_weight_val_2"]
            
        elif side=="bid":
            
            price = row["bid_val_0"]
            count = row["bid_count_0"]        
            if count < amount:
                more_orders = row["bid_count_1"]
                if count+more_orders<=amount:
                    new_count = more_orders
                else:
                    new_count = amount-count
                price = (price * count + row["bid_val_1"]*new_count ) / (count+new_count)
                count += new_count

                if count < amount:
                    more_orders = row["bid_count_2"]
                    if count+more_orders>=amount:
                        new_count = amount-count
                        price = (price * count + row["bid_val_2"]*new_count ) / (count+new_count)
                    else:
                        price = row["bid_weight_val_2"]
        
        return price

    def evaluate(self):

        """
        + Description: Execute algorithm evaluating virtual transfers based on arbitrage.
        + Input:
        -
        + Output:
        - signals: Dictionary of signals returned for the algorithm.
        - params: Dictionary of order parameters.
        """

        # reinitialize signals
        self._reinitialize_signals()

        # reinitialize parameters
        params = {asset:{
            definitions.limit:0,
            definitions.last:0,
            definitions.amount:0
        } for asset in list(self._signals.keys())}

        # asset key should be the same as defined in # Assets in config.py
        asset0 = list(self.assets.keys())[0]
        asset1 = list(self.assets.keys())[1]

        # bases & quotes
        base0 = self.assets[asset0].base
        quote0 = self.assets[asset0].quote
        base1 = self.assets[asset1].base
        quote1 = self.assets[asset1].quote
        
        # quick access to exchange name
        exchange0 = self.assets[asset0].exchange
        exchange1 = self.assets[asset1].exchange

        # quick access to fees
        fee0 = self._fees[exchange0][definitions.trading][definitions.taker]
        fee1 = self._fees[exchange1][definitions.trading][definitions.taker]

        # world_time
        world_time = self._world.get_time()

        if len(self.data_modules[0].data>0) and len(self.data_modules[1].data>0):

            # orderbook0 time
            time0 = self.data_modules[0].data.index[-1]
            # orderbook1 time
            time1 = self.data_modules[1].data.index[-1]

            if world_time >= time0 and\
                world_time >= time1 and\
                world_time-time0<=self._max_delay_in_data and\
                world_time-time1<=self._max_delay_in_data and\
                (time0>self.time0_prev and time1>self.time1_prev): # non repeated request

                # store to compare next round so never use them again
                self.time0_prev = time0
                self.time1_prev = time1

                # Compute amount to trade

                base = base0
                quote = quote0
                aprox_base_price_in_quote = self.data_modules[0].data.iloc[-1]["ask_val_0"]
                asset_usd = self.get_usd_base_value(base, quote, aprox_base_price_in_quote)

                if self._usd_amount_to_trade == definitions.full:
                    raise ValueError("ERROR! You can't use full amount in arbitrage!")
                else:
                    amount = self._usd_amount_to_trade / asset_usd

                # compute prices

                bid0 = self.get_weight_val(self.data_modules[0].data.iloc[-1], "bid", amount)
                ask0 = self.get_weight_val(self.data_modules[0].data.iloc[-1], "ask", amount)

                bid1 = self.get_weight_val(self.data_modules[1].data.iloc[-1], "bid", amount)
                ask1 = self.get_weight_val(self.data_modules[1].data.iloc[-1], "ask", amount)

                # Statistical calculations

                p_l0_s1_actual = -ask0*(1+fee0)+bid1*(1-fee1)
                p_l1_s0_actual = -ask1*(1+fee1)+bid0*(1-fee0)

                self.p_l0_s1 = np.append(self.p_l0_s1, p_l0_s1_actual)
                self.p_l1_s0 = np.append(self.p_l1_s0, p_l1_s0_actual)

                if len(self.p_l0_s1) > self._period: # we have enough data

                    self.p_l0_s1 = np.delete(self.p_l0_s1, 0)
                    self.p_l1_s0 = np.delete(self.p_l1_s0, 0)

                    p_l0_s1_m = np.mean(self.p_l0_s1)
                    p_l1_s0_m = np.mean(self.p_l1_s0)

                    # Analyze open positions

                    if self._positions_are_closed() and self._operating:

                        # if p_l0_s1_actual > -p_l1_s0_m:
                        if p_l0_s1_actual > 0:
                            
                            self._shoot_long_signal(asset0)                
                            params[asset0] = {
                                definitions.amount:amount,
                                definitions.limit:bid0,
                                definitions.last:ask0
                            }

                            self._shoot_short_signal(asset1)
                            params[asset1] = {
                                definitions.amount:amount,
                                definitions.limit:ask1,
                                definitions.last:bid1
                            }
                            
                            self.required_status[definitions.long_position] = asset0
                            self.required_status[definitions.short_position] = asset1
                            self._operating = False

                            self.prev_profit = p_l0_s1_actual
                            self.prev_amount = amount
                        
                        # elif p_l1_s0_actual > -p_l0_s1_m:
                        elif p_l1_s0_actual > 0:
                            
                            self._shoot_short_signal(asset0)
                            params[asset0] = {
                                definitions.amount:amount,
                                definitions.limit:ask0,
                                definitions.last:bid0
                            }

                            self._shoot_long_signal(asset1)
                            params[asset1] = {
                                definitions.amount:amount,
                                definitions.limit:bid1,
                                definitions.last:ask1
                            }

                            self.required_status[definitions.short_position] = asset0
                            self.required_status[definitions.long_position] = asset1
                            self._operating = False

                            self.prev_profit = p_l1_s0_actual
                            self.prev_amount = amount
                    
                    # Analyze close positions
                    elif not self._positions_are_closed() and self._operating:

                        if p_l0_s1_actual + self.prev_profit > 0 and\
                        self.prev_amount*(p_l0_s1_actual + self.prev_profit) > self._min_usd_profit and\
                        self.status[definitions.long_position]==asset1:
                            
                            self._shoot_long_signal(asset0)                
                            params[asset0] = {
                                definitions.amount:self.prev_amount,
                                definitions.limit:bid0,
                                definitions.last:ask0
                            }

                            self._shoot_short_signal(asset1)
                            params[asset1] = {
                                definitions.amount:self.prev_amount,
                                definitions.limit:ask1,
                                definitions.last:bid1,
                            }
                            
                            self.required_status[definitions.long_position] = None
                            self.required_status[definitions.short_position] = None
                            self._operating = False
                        
                        elif p_l1_s0_actual + self.prev_profit > 0 and\
                        self.prev_amount*(p_l1_s0_actual + self.prev_profit) > self._min_usd_profit and\
                        self.status[definitions.long_position]==asset0:

                            self._shoot_short_signal(asset0)
                            params[asset0] = {
                                definitions.amount:self.prev_amount,
                                definitions.limit:ask0,
                                definitions.last:bid0
                            }

                            self._shoot_long_signal(asset1)
                            params[asset1] = {
                                definitions.amount:self.prev_amount,
                                definitions.limit:bid1,
                                definitions.last:ask1
                            }

                            self.required_status[definitions.long_position] = None
                            self.required_status[definitions.short_position] = None
                            self._operating = False
                    
                else:
                    print("Doing nothing. Not enough data yet...")
        
        # example
        
        # self._shoot_short_signal(asset0)
        # params[asset0] = {
        #     definitions.amount:20,
        #     definitions.limit:ask0,
        #     definitions.last:bid0
        # }

        # self._shoot_long_signal(asset1)
        # params[asset1] = {
        #     definitions.amount:20,
        #     definitions.limit:bid1,
        #     definitions.last:ask1
        # }

        # self.required_status[definitions.short_position] = asset0
        # self.required_status[definitions.long_position] = asset1
        # self._operating = False

        return self._signals, params

    def _positions_are_closed(self):

        """
        + Description: Analyze if actual status allow opend positions.
        + Input:
        -      
        + Output:
        - answer: bool True or False depending on opportunity availability.
        """

        if self.status[definitions.long_position] != None:
            return False
        if self.status[definitions.short_position] != None:
            return False

        return True

    def operate_and_confirm_status(self):

        """
        + Description: This function is called from trading module, after confirming posted orders has been executed succesfully.
        + Input:
        -      
        + Output:
        - 
        """

        self.status[definitions.short_position] = self.required_status[definitions.short_position]
        self.status[definitions.long_position] = self.required_status[definitions.long_position]

        self._operating = True


    def operate_and_cancel_status(self):

        """
        + Description: This function is called from trading module, after cancelling posted orders.
        + Input:
        -      
        + Output:
        - 
        """

        self.required_status[definitions.short_position] = None
        self.required_status[definitions.long_position] = None

        self._operating = True