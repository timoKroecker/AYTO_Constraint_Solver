def header():
    print("""
           _____  ____________      
          /   \ \/ /_  __/ __ \     
         / /| |\  / / / / / / /     
        / ___ |/ / / / / /_/ /      
   ____/_/__|_/_/ /_/  \____/______ 
  / ___// __ \/ /| |  / / ____/ __ \\
  \__ \/ / / / / | | / / __/ / /_/ /
 ___/ / /_/ / /__| |/ / /___/ _, _/ 
/____/\____/_____/___/_____/_/ |_|  
                                    
      
""")
    
def init():
    print("")
    season = input("Please enter season: ")
    night = input("Please enter matching night: ")
    print("")
    return season, night

def solver_stats(results, pre_mzn, post_mzn):
    print("num solutions: ", len(results))
    print("minizinc runtime: ", get_duration_string(pre_mzn, post_mzn))

def input_stats(input):
    print("Number of unknown values: ", get_num_zeros(input))

def get_num_zeros(matrix):
    num = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == 0):
                num += 1
    return num

def get_duration_string(pre, post):
    total_seconds = (post.tm_min - pre.tm_min) * 60 + post.tm_sec - pre.tm_sec
    minutes = total_seconds // 60
    seconds = total_seconds - 60 * minutes
    return str(minutes) + "m" + str(seconds) + "s"