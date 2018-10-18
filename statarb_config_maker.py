import definitions

def get_next_valid_line(infile):

  while True:
    line = infile.readline()
    if line:
      try:
        _ = line.split()[0]
        return line
      except:
        pass # newline
    else: # EOF
      return line

two_char_symbols = ["sc"]
four_char_symbols = ["dash", "usdt", "iota", "doge", "nano", "qtum", "npxs"]
five_char_symbols = ["miota", "waves"]
symbols = set()
exchanges = set()
accounts = ["margin", "trading", "funding"]

def get_base(symbol):
    
    if symbol[:2] in two_char_symbols:
      symbols.update([symbol[:2]])
      return symbol[:2]
    
    if symbol[:4] in four_char_symbols:
      symbols.update([symbol[:4]])
      return symbol[:4]
    
    if symbol[:5] in five_char_symbols:
      symbols.update([symbol[:5]])
      return symbol[:5]

    symbols.update([symbol[:3]])
    return symbol[:3]

def get_quote(symbol):
    
    if symbol[-2:] in two_char_symbols:
      symbols.update([symbol[-2:]])
      return symbol[-2:]
    
    if symbol[-4:] in four_char_symbols:
      symbols.update([symbol[-4:]])
      return symbol[-4:]
    
    if symbol[-5:] in five_char_symbols:
      symbols.update([symbol[-5:]])
      return symbol[-5:]

    symbols.update([symbol[-3:]])
    return symbol[-3:]


config_input = "config_maker.hermes"
config_output = "config.py"

with open(config_input, "r") as infile:

  line = get_next_valid_line(infile)
  
  while line:
  
    if line.split()[0] == "data":

      while line.split()[0] != "end":        
        line = get_next_valid_line(infile)

        if line.split()[0] == "data_type":
          data_type = line.split()[1]
        
        elif line.split()[0] == "timeframe":
          timeframe = line.split()[1]
        
        elif line.split()[0] == "data_format":
          data_format = line.split()[1]

        elif line.split()[0] == "header_format":
          header_format = line.split()[1]
        
        elif line.split()[0] == "elements":
          
          elements = []

          line = get_next_valid_line(infile)
          while line.split()[0] != "end":

            elements.append(
              {
                "symbol":line.split()[0],
                "account":line.split()[1],
                "exchange":line.split()[2],
                "file":"\""+line.split()[3]+"\""                
              }
            )
            exchanges.update([line.split()[2]])
            line = get_next_valid_line(infile)

          line = get_next_valid_line(infile)

    elif line.split()[0] == "algorithms":

      while line.split()[0] != "end":        
        line = get_next_valid_line(infile)

        if line.split()[0] == "name":
          algo_name = line.split()[1]
        
        if line.split()[0] == "type":
          algo_type = line.split()[1]

        if line.split()[0] == "signals":
          long_signal = line.split()[1]
          short_signal = line.split()[2]

        elif line.split()[0] == "algo_params":

          line = get_next_valid_line(infile)
          algo_params = {}
          while line.split()[0] != "end":

            algo_params[line.split()[0]] = line.split()[1]

            line = get_next_valid_line(infile)

          line = get_next_valid_line(infile)

    
    elif line.split()[0] == "strategies":
      
      while line.split()[0] != "end":
        line = get_next_valid_line(infile)

        if line.split()[0] == "thresholds":
          long_trs = line.split()[1]
          short_trs = line.split()[2]
        elif line.split()[0] == "order_type":
          order_type = line.split()[1]
    
    elif line.split()[0] == "general_settings":

      while line.split()[0] != "end":
        # line = get_next_valid_line(infile)

        if line.split()[0] == "trading_mode":
          trading_mode = line.split()[1]
        elif line.split()[0] == "n_request_threads":
          n_request_threads = line.split()[1]
        elif line.split()[0] == "time_step":
          time_step = line.split()[1]
        elif line.split()[0] == "virtual_portfolio":
          virtual_portfolio = line.split()[1]

        elif line.split()[0] == "virtual_tickers":          

          line = get_next_valid_line(infile)
          tickers = {}
          while line.split()[0] != "end":
            
            tickers[line.split()[0]] = line.split()[1]
            line = get_next_valid_line(infile)

        elif line.split()[0] == "api_keys_files":

          line = get_next_valid_line(infile)
          api_keys_files = {}
          while line.split()[0] != "end":
            
            api_keys_files[line.split()[0]] = "\""+line.split()[1]+"\""
            line = get_next_valid_line(infile)

        elif line.split()[0] == "uid_files":

          line = get_next_valid_line(infile)
          uid_files = {}
          while line.split()[0] != "end":
            
            uid_files[line.split()[0]] = "\""+line.split()[1]+"\""
            line = get_next_valid_line(infile)

        line = get_next_valid_line(infile)

    line = get_next_valid_line(infile)
    
outfile = open(config_output, "w")
outfile.write("from definitions import *\n")
outfile.write("\n")
outfile.write("\n")


outfile.write("#######################################################\n")
outfile.write("#                  DATA SECTION\n")
outfile.write("#######################################################\n\n")

outfile.write("data_elements = {\n")
for element in elements:
  e_name = "\""+data_type+"_"+element["symbol"]+"_"+element["exchange"]+"\""
  outfile.write("\t"+e_name+":{\n")
  outfile.write("\t\t"+"description: "+element["symbol"]+",\n")
  outfile.write("\t\t"+"source: "+element["exchange"]+",\n")
  outfile.write("\t\t"+"data_type: "+data_type+",\n")
  outfile.write("\t\t"+"timeframe: "+timeframe+",\n")
  outfile.write("\t\t"+"data_format: "+data_format+",\n")
  outfile.write("\t\t"+"header_format: "+header_format+",\n")
  outfile.write("\t\t"+"file_name: "+element["file"]+",\n")
  outfile.write("\t},\n")
outfile.write("}\n")
outfile.write("\n")

outfile.write("#######################################################\n")
outfile.write("#                  ASSETS SECTION\n")
outfile.write("#######################################################\n\n")

outfile.write("assets_elements = {\n")
for element in elements:
  a_name = "\""+element["symbol"]+"_"+element["exchange"]+"\""
  outfile.write("\t"+a_name+":{\n")
  outfile.write("\t\t"+"symbol: "+element["symbol"]+",\n")
  outfile.write("\t\t"+"base: "+get_base(element["symbol"])+",\n")
  outfile.write("\t\t"+"quote: "+get_quote(element["symbol"])+",\n")
  outfile.write("\t\t"+"exchange: "+element["exchange"]+",\n")
  outfile.write("\t\t"+"account: "+element["account"]+",\n")
  outfile.write("\t},\n")
outfile.write("}\n")
outfile.write("\n")


outfile.write("#######################################################\n")
outfile.write("#                  ALGORITHMS SECTION\n")
outfile.write("#######################################################\n\n")

outfile.write("algorithms_elements = {\n")
algo=0
algorithms = []
for i, i_element in enumerate(elements[:-1]):
  for j_element in elements[i+1:]:
    
    # check both pairs belong to an arbitrage pair
    if i_element["symbol"]==j_element["symbol"]:

      al_name = "\""+algo_name+"_"+str(algo)+"\""
      outfile.write("\t"+al_name+":{\n")
      outfile.write("\t\t"+"algorithm: "+algo_type+",\n")
      outfile.write("\t\t"+"data_modules_array: ["+"\n")
      outfile.write("\t\t\t"+"\""+data_type+"_"+i_element["symbol"]+"_"+i_element["exchange"]+"\",\n")
      outfile.write("\t\t\t"+"\""+data_type+"_"+j_element["symbol"]+"_"+j_element["exchange"]+"\"\n")
      outfile.write("\t\t"+"],\n")
      outfile.write("\t\t"+"signals: {"+"\n")
      outfile.write("\t\t\t"+"\""+i_element["symbol"]+"_"+i_element["exchange"]+"\":{\n")
      outfile.write("\t\t\t\t"+"long_signal:"+long_signal+",\n")
      outfile.write("\t\t\t\t"+"short_signal:"+short_signal+",\n")
      outfile.write("\t\t\t"+"},\n")
      outfile.write("\t\t\t"+"\""+j_element["symbol"]+"_"+j_element["exchange"]+"\":{\n")
      outfile.write("\t\t\t\t"+"long_signal:"+long_signal+",\n")
      outfile.write("\t\t\t\t"+"short_signal:"+short_signal+",\n")
      outfile.write("\t\t\t"+"},\n")
      outfile.write("\t\t"+"},\n")
      outfile.write("\t\t"+"algo_params: {"+"\n")
      for param_key, param_val in algo_params.items():
        outfile.write("\t\t\t"+param_key+":"+param_val+",\n")
      outfile.write("\t\t"+"},\n")
      outfile.write("\t},\n")
      algo+=1
      algorithms.append({"name":al_name,
                        "elem0":"\""+i_element["symbol"]+"_"+i_element["exchange"]+"\"",
                        "elem1":"\""+j_element["symbol"]+"_"+j_element["exchange"]+"\""})
outfile.write("}\n")
outfile.write("\n")


outfile.write("#######################################################\n")
outfile.write("#                  STRATEGIES SECTION\n")
outfile.write("#######################################################\n\n")

outfile.write("strategies_elements = {\n")
strat=0
for algorithm in algorithms:

  s_name = "\""+"strategy"+"_"+str(strat)+"\""
  outfile.write("\t"+s_name+":{\n")
  outfile.write("\t\t"+"algorithms_array:"+"["+algorithm["name"]+"],\n")
  outfile.write("\t\t"+"thresholds:{\n")
  outfile.write("\t\t\t"+algorithm["elem0"]+":{\n")
  outfile.write("\t\t\t\t"+"long_threshold:"+long_trs+",\n")
  outfile.write("\t\t\t\t"+"short_threshold:"+short_trs+"\n")
  outfile.write("\t\t\t"+"},\n")
  outfile.write("\t\t\t"+algorithm["elem1"]+":{\n")
  outfile.write("\t\t\t\t"+"long_threshold:"+long_trs+",\n")
  outfile.write("\t\t\t\t"+"short_threshold:"+short_trs+"\n")
  outfile.write("\t\t\t"+"}\n")
  outfile.write("\t\t"+"},\n")
  outfile.write("\t\t"+"order_type:"+order_type+"\n")
  
  outfile.write("\t},\n")
  strat+=1
outfile.write("}\n")
outfile.write("\n")

outfile.write("#######################################################\n")
outfile.write("#                  GENERAL SETTINGS\n")
outfile.write("#######################################################\n\n")

outfile.write("trading_mode = "+trading_mode+"\n")
outfile.write("n_request_threads = "+n_request_threads+"\n")
outfile.write("\n")

outfile.write("#######################################################\n")
outfile.write("#                  BACKTEST SECTION\n")
outfile.write("#######################################################\n\n")

outfile.write("time_step = "+time_step+"\n")
outfile.write("virtual_portfolio = {\n")

for exchange in exchanges:
  outfile.write("\t"+exchange+":{\n")
  for account in accounts:
    outfile.write("\t\t"+account+":{\n")
    for symbol in symbols:
      outfile.write("\t\t\t"+symbol+":{\n")
      outfile.write("\t\t\t\t"+"free:9999999,\n")
      outfile.write("\t\t\t\t"+"used:0,\n")
      outfile.write("\t\t\t\t"+"total:9999999\n")
      outfile.write("\t\t\t"+"},\n")
    outfile.write("\t\t"+"},\n")
  outfile.write("\t"+"},\n")
outfile.write("}\n")

outfile.write("virtual_tickers = {\n")
for ticker_key, ticker_val in tickers.items():
  outfile.write("\t"+ticker_key+":{\n")
  outfile.write("\t\t"+"last:"+ticker_val+"\n")
  outfile.write("\t},\n")
outfile.write("}\n")

outfile.write("\n")
outfile.write("\n")


outfile.write("#######################################################\n")
outfile.write("#                  PAPER TRADING SECTION\n")
outfile.write("#######################################################\n\n")

outfile.write("\n")
outfile.write("\n")

outfile.write("#######################################################\n")
outfile.write("#                  REAL TRADING SECTION\n")
outfile.write("#######################################################\n\n")

outfile.write("api_keys_files = {\n")
for exchange, key in api_keys_files.items():
  outfile.write("\t"+exchange+": "+key+",\n")
outfile.write("}\n")
outfile.write("uid_files = {\n")
for exchange, uid in uid_files.items():
  outfile.write("\t"+exchange+": "+uid+",\n")
outfile.write("}\n")
outfile.write("\n")
outfile.write("\n")

outfile.close()