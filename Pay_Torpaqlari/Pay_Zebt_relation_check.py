import arcpy

class Pay_zebt_relcheck:
    def __init__(self,base_data_path,error_data_path):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'

        self.check_with_relation(base_data_path,error_data_path)
        
    
    def check_with_relation(self,base_data_path,error_data_path):
        arcpy.management.MakeFeatureLayer(base_data_path+"\Pay_torpaqi","Pay_make6")
        arcpy.management.MakeFeatureLayer(base_data_path+"\Zebt","Zebt1")
        
        pay_parselid = arcpy.management.SelectLayerByAttribute("Pay_make6", 'NEW_SELECTION',"Parsel_id is null", 'NON_INVERT')
        zebt_fkparsel = arcpy.management.SelectLayerByAttribute("Zebt1", 'NEW_SELECTION',"Fk_Parsel is null", 'NON_INVERT')
       
        
        count_pay_parselid = arcpy.GetCount_management(pay_parselid)
        
        count_zebt_fkparsel = arcpy.GetCount_management(zebt_fkparsel)
        
        if str(count_pay_parselid) != "0" or str(count_zebt_fkparsel) != "0":
            print("Parsel ve ya zebt layinda relation sutunlarinda bos olan row-lar var.")
            
            
        if str(count_pay_parselid) == "0" and str(count_zebt_fkparsel) == "0":
            
            arcpy.management.AddJoin("Pay_make6", 'Parsel_id', "Zebt1", 'Fk_Parsel', 'KEEP_ALL')
            expression = "(Pay_torpaqi.Jn <> Zebt.Jn) or (Pay_torpaqi.Rn <> Zebt.Rn) or (Pay_torpaqi.Cn <> Zebt.Cn)"

            checkjnrncn = arcpy.management.SelectLayerByAttribute("Pay_make6", 'NEW_SELECTION',expression, 'NON_INVERT')
                
            if checkjnrncn:
                arcpy.management.CopyFeatures("Pay_make6",error_data_path+"\Pay_torpagi_ile_Zebt_arasinda_Jn_Rn_Cn_ferqleri")
                arcpy.management.RemoveJoin("Pay_make6", "Zebt")
                    
            arcpy.management.SelectLayerByAttribute("Pay_make6", 'CLEAR_SELECTION')
            arcpy.management.SelectLayerByAttribute("Zebt1", 'CLEAR_SELECTION')
                
                    
                    
                    
            arcpy.management.AddJoin("Zebt1", 'Fk_Parsel', "Pay_make6", 'Parsel_id', 'KEEP_ALL')
            check_not_join = arcpy.management.SelectLayerByAttribute("Zebt1", 'NEW_SELECTION',"Pay_torpaqi.Shape_Area is null", 'NON_INVERT')
            
            if check_not_join:
                arcpy.management.CopyFeatures("Zebt1",error_data_path+"\Join_Olunmayan_Zebtler")
                arcpy.management.SelectLayerByAttribute("Zebt1", 'CLEAR_SELECTION')
                
            check_noksan = arcpy.management.SelectLayerByAttribute("Zebt1", 'NEW_SELECTION',"Pay_torpaqi.Shape_Area is not null", 'NON_INVERT')
            
            if check_noksan:
                arcpy.management.SelectLayerByAttribute("Zebt1", 'SUBSET_SELECTION',"Pay_torpaqi.Noksan = 1", 'NON_INVERT')
                arcpy.management.CopyFeatures("Zebt1",error_data_path+"\Zebtin_payi_Noksanlidir_Bu_Halda_Zebt_Olmamalidir")
                arcpy.management.RemoveJoin("Zebt1", "Pay_torpaqi")
                arcpy.management.SelectLayerByAttribute("Zebt1", 'CLEAR_SELECTION')
            
            
            
        
                
        
            
        