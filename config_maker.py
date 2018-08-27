import definitions

config_input = "config_maker.hermes"
config_output = "config.py"

with open(config_input, "r") as infile:

  line = infile.readline()
  while line:

    if line.split()[0] == "data":

      while line.split()[0] != "end":
        line = infile.readline()

        if line.split()[0] == "data_type":
          data_type = line.split()[1]
        
        elif line.split()[0] == "timeframe":
          timeframe = line.split()[1]
        
        elif line.split()[0] == "data_format":
          data_format = line.split()[1]

        elif line.split()[0] == "header_format":
          header_format = line.split()[1]
        
        elif line.split()[0] == "header_format":
          header_format = line.split()[1]
        
        elif line.split()[0] == "elements":
          
          symbols = []
          exchanges = []
          files = []

          line = infile.readline()
          while line.split()[0] != "end": 

            symbols.append(line.split()[0])
            exchanges.append(line.split()[1])
            files.append(line.split()[2])
            line = infile.readline()

          line = infile.readline()

    elif line.split()[0] == "algorithms":

      pass

    
    elif line.split()[0] == "strategies":

      pass

    
    elif line == "general_settings":

      pass

    line = infile.readline()

    
outfile = open(config_output, "w")
outfile.write("from definitions import *\n")
outfile.write("\n")
outfile.write("\n")


outfile.write("#######################################################\n")
outfile.write("#                  DATA SECTION\n")
outfile.write("#######################################################\n")
outfile.write(str(exchanges))


outfile.write("#######################################################\n")
outfile.write("#                  ALGORITHMS SECTION\n")
outfile.write("#######################################################\n")


outfile.write("#######################################################\n")
outfile.write("#                  STRATEGIES SECTION\n")
outfile.write("#######################################################\n")

outfile.close()