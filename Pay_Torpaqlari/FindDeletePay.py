import arcpy

class FindDelete_pay:
    def __init__(self,base_data_path,error_data_path,trash_data_path,newpay,oldpay,itmim):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'

        self.FindPay(base_data_path,error_data_path,trash_data_path,newpay,oldpay,itmim)
        
    
    def FindPay(self,base_data_path,error_data_path,trash_data_path,newpay,oldpay,itmim):
        oldpay_ = []
        newpay_ = []
        
        arcpy.env.workspace = newpay
        featureclasses2 = arcpy.ListFeatureClasses()
        for fc2 in featureclasses2:
            newpay_.append(fc2)
            newpay_.sort()
        print(newpay_)
            
            
        arcpy.env.workspace = oldpay
        featureclasses3 = arcpy.ListFeatureClasses()
        for fc3 in featureclasses3:
            oldpay_.append(fc3)
            oldpay_.sort()
            
        print(oldpay_)
            
            
        count_newpay = len(newpay_)
        
        n = 0
        
        while n < count_newpay:
            arcpy.management.MakeFeatureLayer(newpay + "/" +str(newpay_[n]),newpay_[n]+str(n)+"compare")
            arcpy.management.MakeFeatureLayer(oldpay + "/" +str(oldpay_[n]),oldpay_[n]+str(n)+"compare")
            
            arcpy.management.AddJoin(oldpay_[n]+str(n)+"compare", 'Jn' , newpay_[n]+str(n)+"compare", 'Jn' , 'KEEP_ALL')
            
            selectshapeNotnull = arcpy.management.SelectLayerByAttribute(oldpay_[n]+str(n)+"compare", 'NEW_SELECTION',"{}.SHAPE_Area IS NOT NULL".format(newpay_[n]), 'NON_INVERT')
        
            count_selectshapeNotnull = arcpy.GetCount_management(selectshapeNotnull)
            
            if str(count_selectshapeNotnull) !="0":
                arcpy.management.CopyFeatures(oldpay_[n]+str(n)+"compare",itmim+"\{}_silinmeli".format(oldpay_[n]))
                arcpy.management.DeleteRows(oldpay_[n]+str(n)+"compare")
                
            ######## yeni yazdiqlarim Rn ucun #######
                
            arcpy.management.RemoveJoin(oldpay_[n]+str(n)+"compare",str(newpay_[n]))
                
                
            arcpy.management.AddJoin(oldpay_[n]+str(n)+"compare", 'Rn' , newpay_[n]+str(n)+"compare", 'Rn' , 'KEEP_ALL')
            
            selectshapeNotnull_Rn = arcpy.management.SelectLayerByAttribute(oldpay_[n]+str(n)+"compare", 'NEW_SELECTION',"{}.SHAPE_Area IS NOT NULL".format(newpay_[n]), 'NON_INVERT')
            
            count_selectshapeNotnull_rn = arcpy.GetCount_management(selectshapeNotnull_Rn)
            
            if str(count_selectshapeNotnull_rn) !="0":
                arcpy.management.CopyFeatures(oldpay_[n]+str(n)+"compare",itmim+"\{}_silinmeli_rn".format(oldpay_[n]))
                arcpy.management.DeleteRows(oldpay_[n]+str(n)+"compare")
                
                arcpy.management.Append(itmim+"\{}_silinmeli_rn".format(oldpay_[n]), itmim+"\{}_silinmeli".format(oldpay_[n]), 'NO_TEST')
                
                arcpy.management.Delete(itmim+"\{}_silinmeli_rn".format(oldpay_[n]))
                
            ######## yeni yazdiqlarim Rn ucun #######
            
            ######## yeni yazdiqlarim Cn ucun #######
            
            arcpy.management.RemoveJoin(oldpay_[n]+str(n)+"compare",str(newpay_[n]))
                
                
            arcpy.management.AddJoin(oldpay_[n]+str(n)+"compare", 'Cn' , newpay_[n]+str(n)+"compare", 'Cn' , 'KEEP_ALL')
            
            selectshapeNotnull_Cn = arcpy.management.SelectLayerByAttribute(oldpay_[n]+str(n)+"compare", 'NEW_SELECTION',"{}.SHAPE_Area IS NOT NULL".format(newpay_[n]), 'NON_INVERT')
            
            count_selectshapeNotnull_cn = arcpy.GetCount_management(selectshapeNotnull_Cn)
            
            if str(count_selectshapeNotnull_cn) !="0":
                arcpy.management.CopyFeatures(oldpay_[n]+str(n)+"compare",itmim+"\{}_silinmeli_cn".format(oldpay_[n]))
                arcpy.management.DeleteRows(oldpay_[n]+str(n)+"compare")
                
                arcpy.management.Append(itmim+"\{}_silinmeli_cn".format(oldpay_[n]), itmim+"\{}_silinmeli".format(oldpay_[n]), 'NO_TEST')
                
                arcpy.management.Delete(itmim+"\{}_silinmeli_cn".format(oldpay_[n]))
                
            
            arcpy.management.RemoveJoin(oldpay_[n]+str(n)+"compare",str(newpay_[n]))
            
            ######## yeni yazdiqlarim Cn ucun #######
                
                
            ######### kesisen kohne paylari tapiriq ################
            
            arcpy.analysis.Intersect([oldpay_[n]+str(n)+"compare",newpay_[n]+str(n)+"compare"],error_data_path+"\{}_Kohne_pay_yeni_payla_kesisir".format(oldpay_[n]))    

     
            count_pay_intersect = arcpy.GetCount_management(error_data_path+"\{}_Kohne_pay_yeni_payla_kesisir".format(oldpay_[n]))
            
            if str(count_pay_intersect) != "0":
                arcpy.management.Delete(error_data_path+"\{}_Kohne_pay_yeni_payla_kesisir".format(oldpay_[n]))
                
                
            ######### kesisen kohne paylari tapiriq ################
            
            arcpy.analysis.TabulateIntersection(oldpay + "/" +str(oldpay_[n]), 'OBJECTID', newpay + "/" +str(newpay_[n]),trash_data_path+"\{}_OldPayTabulate".format(str(oldpay_[n]))+str(n))
            arcpy.management.AddJoin(oldpay_[n]+str(n)+"compare", 'OBJECTID', trash_data_path+"\{}_OldPayTabulate".format(str(oldpay_[n]))+str(n), 'OBJECTID_1', 'KEEP_ALL')
            
            checkpercentace = arcpy.management.SelectLayerByAttribute(oldpay_[n]+str(n)+"compare", 'NEW_SELECTION',"PERCENTAGE > 40", 'NON_INVERT')
            
            count_checkpercentace = arcpy.GetCount_management(checkpercentace)
            
            if str(count_checkpercentace) !="0":
                arcpy.management.DeleteRows(oldpay_[n]+str(n)+"compare")
                arcpy.management.RemoveJoin(oldpay_[n]+str(n)+"compare","{}_OldPayTabulate".format(str(oldpay_[n]))+str(n))
            
                
                
            n+=1
            
        