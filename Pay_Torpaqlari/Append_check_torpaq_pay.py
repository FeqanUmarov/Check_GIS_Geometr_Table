import arcpy

class Append_check_Process:
    def __init__(self,base_data_path,error_data_path,trash_data_path,newpay,oldpay):
        super().__init__()

        self.merge_pay(newpay,oldpay,trash_data_path)
        
        self.merge_torpaq(base_data_path,error_data_path,trash_data_path)
        
    
    def merge_pay(self,newpay,oldpay,trash_data_path):
        oldpay_forappend = []
        newpay_forappend = []
        
        arcpy.env.workspace = newpay
        featureclasses3 = arcpy.ListFeatureClasses()
        for fc3 in featureclasses3:
            newpay_forappend.append(fc3)
            newpay_forappend.sort()
            
            
            
        arcpy.env.workspace = oldpay
        featureclasses4 = arcpy.ListFeatureClasses()
        for fc4 in featureclasses4:
            oldpay_forappend.append(fc4)
            oldpay_forappend.sort()
            
        
        count_newpay1 = len(newpay_forappend)
        count_newpay2 = len(oldpay_forappend)
        
        if count_newpay1 == count_newpay2:
        
            n = 0
            
            while count_newpay2 > n:                                                           
                
                arcpy.management.Append(newpay+'/'+ newpay_forappend[n], oldpay+'/' + oldpay_forappend[n], 'NO_TEST')
                
                n+=1
        
            k = 1
            
            while count_newpay2 > k:
                
                arcpy.management.Append(oldpay+'/' + oldpay_forappend[k], oldpay+'/'+ oldpay_forappend[0], 'NO_TEST')
                
                k+=1
                
            
            arcpy.management.CopyFeatures(oldpay+'/'+ oldpay_forappend[0],trash_data_path+"\Butov_pay")
                
                
    
    def merge_torpaq(self,base_data_path,error_data_path,trash_data_path):
        
        ### erase torpaq serhed #######
        arcpy.management.MakeFeatureLayer(base_data_path + "\TORPAQ_TUM","TorpaqYeni3")
        arcpy.management.CopyFeatures(base_data_path + "\Torpaq_Kohne",trash_data_path+"\Torpaq_Kohne_copy")
        arcpy.management.MakeFeatureLayer(trash_data_path+"\Torpaq_Kohne_copy","TorpaqKohne3")

        arcpy.analysis.TabulateIntersection(trash_data_path+"\Torpaq_Kohne_copy", 'OBJECTID', base_data_path + "\TORPAQ_TUM",trash_data_path+"\intersect_tabulate_torpaq")
        
        arcpy.management.AddJoin("TorpaqKohne3", 'OBJECTID' , trash_data_path+"\intersect_tabulate_torpaq", 'OBJECTID_1' , 'KEEP_ALL')
        
        arcpy.management.SelectLayerByAttribute("TorpaqKohne3", 'NEW_SELECTION',"intersect_tabulate_torpaq.PERCENTAGE > 4", 'NON_INVERT')
        
        arcpy.management.DeleteRows("TorpaqKohne3")
        
        arcpy.management.RemoveJoin("TorpaqKohne3","intersect_tabulate_torpaq")
        
        arcpy.management.AlterField('TorpaqKohne3', 'FK_LANDUSAGE_TYPE','T_KATEGORI')
        
        arcpy.management.AlterField('TorpaqKohne3', 'FK_OWNERSHIP_TYPE','MULKFORM')
        
        
        
        arcpy.management.Append("TorpaqYeni3", "TorpaqKohne3", 'NO_TEST')
        
        arcpy.management.CopyFeatures("TorpaqKohne3",trash_data_path+"\Birlesmis_Torpaq")
        
        arcpy.analysis.Erase(base_data_path+'\Ev_Serheddi', 'TorpaqKohne3',error_data_path+"\Serhed_ile_torpaq_arasinda_bosluqlar")
        
        arcpy.analysis.Erase('TorpaqKohne3', base_data_path+'\Ev_Serheddi',error_data_path+"\Torpaq_Serhedden_Kenara_Cixir")
        
        arcpy.analysis.Intersect(["TorpaqKohne3"],error_data_path+"\Torpaqda_Kesismeler")  
        
        
        
        
        ############ intersect. erase pay zebt ########
        arcpy.management.SelectLayerByAttribute("TorpaqKohne3",'NEW_SELECTION',"T_KATEGORI = 0 and MULKFORM = 2", 'NON_INVERT')
        
        arcpy.management.CopyFeatures("TorpaqKohne3",trash_data_path+"\Birlesmis_Torpaq_Kend_Teserrufati")
        
        arcpy.analysis.Erase(trash_data_path+"\Birlesmis_Torpaq_Kend_Teserrufati", trash_data_path+"\Butov_pay" ,error_data_path+"\Torpaq_Xususidir_Ustunde_Pay_Yoxdur")
        
        arcpy.analysis.Erase(trash_data_path+"\Butov_pay", trash_data_path+"\Birlesmis_Torpaq_Kend_Teserrufati",error_data_path+"\Pay_Torpaqdan_Kenara_Cixir")
        
        arcpy.management.MakeFeatureLayer(trash_data_path+"\Butov_pay","PayTam")
        
        arcpy.analysis.Intersect(["PayTam"],error_data_path+"\Pay_Torpaqlari_Kesisirler")
        
        
            
            
        