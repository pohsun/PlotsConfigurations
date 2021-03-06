# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
   
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                         'fold' : 3
                        }

variables['met']  = {   'name': 'metPfType1',            #   variable name    
                        'range' : (20,0,200),    #   variable range
                        'xaxis' : 'pfmet [GeV]',  #   x axis name
                        'fold' : 0
                        }

variables['zveto_3l']  = {   'name': 'zveto_3l',            #   variable name    
                        'range' : (20,0,100),    #   variable range
                        'xaxis' : 'm_{ll} - M_{Z} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['mllmin3l']  = {   'name': 'mllmin3l',            #   variable name    
                        'range' : (20,10,200),    #   variable range
                        'xaxis' : 'min m_{ll} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['mlll']  = {   'name': 'mlll',            #   variable name    
                        'range' : (50,0.,1000),    #   variable range
                        'xaxis' : 'm_{lll} [GeV]',  #   x axis name
                        'fold' : 0
                        }

variables['njet_3l'] = { 'name': 'njet_3l',      
                        'range' : (8,0,8),  
                        'xaxis' : 'N_Jets', 
                        'fold' : 3
                        }

variables['drllmin3l']  = {   'name': 'drllmin3l',            #   variable name    
                        'range' : (4,0,4),    #   variable range
                        'xaxis' : 'min #Delta Rm_{ll} [GeV]',  #   x axis name
                         'fold' : 0
                        }
