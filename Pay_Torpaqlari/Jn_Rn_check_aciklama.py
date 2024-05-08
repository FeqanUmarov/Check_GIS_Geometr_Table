import arcpy

class Pay_jnrnaciklama:
    def __init__(self,base_data_path,error_data_path):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'

        self.checkjnrnaciklama(base_data_path,error_data_path)
        
    
    def checkjnrnaciklama(self,base_data_path,error_data_path):
        arcpy.management.MakeFeatureLayer(base_data_path+"\Pay_torpaqi","Pay_make")
        arcpy.management.SelectLayerByAttribute("Pay_make", 'NEW_SELECTION',"Jn IS NULL And Rn IS NOT NULL And Aciklama IS NULL", 'NON_INVERT')
        
        count_property = arcpy.GetCount_management("Pay_make")

        count_property1 = str(count_property)
        print(count_property1)
        
        if count_property1 != "0":
            arcpy.management.CopyFeatures("Pay_make",error_data_path+"\Reyestr_hansi_JN_den_alinibsa_aciklamada_qeyd_edilsin")
        