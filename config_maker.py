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
          
          symbols = []
          exchanges = []
          files = []

          line = get_next_valid_line(infile)
          while line.split()[0] != "end":

            symbols.append(line.split()[0])
            exchanges.append(line.split()[1])
            files.append(line.split()[2])
            line = get_next_valid_line(infile)

          line = get_next_valid_line(infile)


    elif line.split()[0] == "algorithms":

      while line.split()[0] != "end":        
        line = get_next_valid_line(infile)

        if line.split()[0] == "signals":
          long_signal = line.split()[1]
          short_signal = line.split()[2]

        elif line.split()[0] == "algo_params":

          line = get_next_valid_line(infile)
          while line.split()[0] != "end":

            if line.split()[0] == "limit_buy_pct":
              limit_buy_pct = line.split()[1]
            elif line.split()[0] == "limit_sell_pct":
              limit_sell_pct = line.split()[1]
            elif line.split()[0] == "max_delay_in_data":
              max_delay_in_data = line.split()[1]
            elif line.split()[0] == "usd_amount_to_trade":
              usd_amount_to_trade = line.split()[1]
            elif line.split()[0] == "period":
              period = line.split()[1]

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
        line = get_next_valid_line(infile)

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

          # line = get_next_valid_line(infile)

        elif line.split()[0] == "api_keys_files":
          print("aoisdoasd")

          line = get_next_valid_line(infile)
          api_keys_files = {}
          while line.split()[0] != "end":
            
            api_keys_files[line.split()[0]] = line.split()[1]
            line = get_next_valid_line(infile)

        line = get_next_valid_line(infile)

    line = get_next_valid_line(infile)

print(api_keys_files)

    
outfile = open(config_output, "w")
outfile.write("from definitions import *\n")
outfile.write("\n")
outfile.write("\n")


outfile.write("#######################################################\n")
outfile.write("#                  DATA SECTION\n")
outfile.write("#######################################################\n")
outfile.write(str(exchanges)+"\n")


outfile.write("#######################################################\n")
outfile.write("#                  ALGORITHMS SECTION\n")
outfile.write("#######################################################\n")


outfile.write("#######################################################\n")
outfile.write("#                  STRATEGIES SECTION\n")
outfile.write("#######################################################\n")

outfile.close()