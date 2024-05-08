import arcpy

class Iha_Ha:
    def __init__(self,base_data_path,error_data_path):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'

        self.check_Iha_Ha(base_data_path,error_data_path)
        
    
    def check_Iha_Ha(self,base_data_path,error_data_path):
        arcpy.management.MakeFeatureLayer(base_data_path+"\Pay_torpaqi","Pay_torpagi3")
        arcpy.management.CalculateField("Pay_torpagi3", 'Ha','round(!Shape_Area!/10000,2)')
        arcpy.management.AddField("Pay_torpagi3","Yoxlama", 'DOUBLE')
        arcpy.management.CalculateField("Pay_torpagi3", 'Yoxlama','!I_Ha!-!Ha!')
        
        cases = ['Yoxlama>0 and Noksan<>1','Yoxlama=0 and Noksan<>0','Yoxlama<0','Noksan is null']
        
        for query in cases:
        
            checkcase = arcpy.management.SelectLayerByAttribute("Pay_torpagi3", 'NEW_SELECTION',query, 'NON_INVERT')
            
            count_checkcase = arcpy.GetCount_management(checkcase)
            
            if str(count_checkcase)!="0" and query == cases[0]:
                print(type(checkcase))
                arcpy.management.CopyFeatures("Pay_torpagi3",error_data_path+"\Payda_Noksan_bir_olmalidir")
                arcpy.management.SelectLayerByAttribute("Pay_torpagi3", 'CLEAR_SELECTION')
                print("1-ci sert")
                
                
            
            elif str(count_checkcase)!="0" and query == cases[1]:
                print(type(checkcase))
                arcpy.management.CopyFeatures("Pay_torpagi3",error_data_path+"\Payda_Noksan_sifir_olmalidir")
                arcpy.management.SelectLayerByAttribute("Pay_torpagi3", 'CLEAR_SELECTION')
                print("2-ci sert")
                
                
            elif str(count_checkcase)!="0" and query == cases[2]:
                print(type(checkcase))
                arcpy.management.CopyFeatures("Pay_torpagi3",error_data_path+"\Ha_I_Ha_dan_Boyuk_Olmaz")
                arcpy.management.SelectLayerByAttribute("Pay_torpagi3", 'CLEAR_SELECTION')
                print("3-ci sert")
                
            elif str(count_checkcase)!="0" and query == cases[3]:
                arcpy.management.CopyFeatures("Pay_torpagi3",error_data_path+"\Payda_Noksan_Bos_Olmaz")
                arcpy.management.SelectLayerByAttribute("Pay_torpagi3", 'CLEAR_SELECTION')
            
            
        