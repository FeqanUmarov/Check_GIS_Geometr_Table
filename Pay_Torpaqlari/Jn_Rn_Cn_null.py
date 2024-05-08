import arcpy

class Pay_jnrncn:
    def __init__(self,base_data_path,error_data_path):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'

        self.check_jn_rn_cn(base_data_path,error_data_path)
        
    
    def check_jn_rn_cn(self,base_data_path,error_data_path):
        arcpy.management.MakeFeatureLayer(base_data_path+"\Pay_torpaqi","Pay_make1")
        arcpy.management.SelectLayerByAttribute("Pay_make1", 'NEW_SELECTION',"Jn IS NULL And Rn IS NULL And Cn IS NULL", 'NON_INVERT')
        
        count_property = arcpy.GetCount_management("Pay_make1")

        count_property1 = str(count_property)
        print(count_property1)
        
        if count_property1 != "0":
            arcpy.management.CopyFeatures("Pay_make1",error_data_path+"\Reyestr_hansi_JN_den_alinibsa_aciklamada_qeyd_edilsin")
        