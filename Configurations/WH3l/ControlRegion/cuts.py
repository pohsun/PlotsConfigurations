# cuts

#cuts = {}
  
supercut = 'mllmin3l>12  \
            && pt1>20 && pt2>15 \
            && pt3>10 \
            && std_vector_lepton_pt[3]<10 \
           '

#cuts['wh3l_top_13TeV']  = 'njet_3l > 0\
#                         && (std_vector_jet_cmvav2[0] > -0.715 || std_vector_jet_cmvav2[1] > -0.715 || std_vector_jet_cmvav2[2] > -0.715 || std_vector_jet_cmvav2[3] > -0.715 || std_                            vector_jet_cmvav2[4] > -0.715 || std_vector_jet_cmvav2[5] || std_vector_jet_cmvav2[6] > -0.715 || std_vector_jet_cmvav2[7] > -0.715 || std_vector_jet_cmv                            av2[8] > -0.715 || std_vector_jet_cmvav2[9] > -0.715) \
#                        && metPfType1 > 30\
#                        && zveto_3l > 20\
 #                     '

cuts['wh3l_wz_13TeV'] = '1'

#cuts['wh3l_wz_13TeV'] = 'njet_3l == 0\
#                         && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
#                         && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
#                         && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
#                         && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
#                         && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
#                         && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
#                         && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
#                         && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
#                         && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
#                         && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
#                         && metPfType1 > 30\
#                         && zveto_3l < 20\
#                         && abs(chlll) == 1\
#                         && mlll > 100\
#                        '


#cuts['wh3l_wz_13TeV'] = 'njet_3l == 0\
#                        && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
#                        && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
#                        && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
#                        && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
#                        && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
#                        && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
#                        && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
#                        && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
#                        && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
#                        && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
#                        && metPfType1 > 30\
#                        && zveto_3l < 20\
#                        && abs(chlll) == 1\
#                        && mlll > 100\
#                       '

#cuts['wh3l_zg_13TeV'] = 'njet_3l == 0\
#                        && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
#                        && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
#                        && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
#                        && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
#                        && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
#                        && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
#                        && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
#                        && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
#                        && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
#                        && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
#                        && metPfType1 < 40\
#                        && mlll > 80\
#                        && mlll < 100\
#                        && abs(chlll) == 1\
#                       '

#cuts['wh3l_zjets_13TeV'] = 'njet_3l == 0\
#                        && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
#                        && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
#                        && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
#                        && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
#                        && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
#                        && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
#                        && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
#                        && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
#                        && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
#                        && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
#                        && metPfType1 < 35\
#                        && zveto_3l < 20\
#                       '
# 11 = e
# 13 = mu
# 15 = tau

