import arcpy


class Check_New_Old_Pay:
    def __init__(self,base_data_path,error_data_path,trash_data_path,newpay,oldpay):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'

        self.new_old_pay_check(base_data_path,error_data_path,trash_data_path,newpay,oldpay)
        
    
    def new_old_pay_check(self,base_data_path,error_data_path,trash_data_path,newpay,oldpay):
        
        newpayname = []
        oldpayname = []
        
        additional_text_new_pay = "Yeni"
        additional_text_old_pay = "Kohne"
        
        ##################################### Yeni paylar #############################################
        arcpy.CalculateField_management(base_data_path+"\Ev_Serheddi", "Adi", '!' + "Adi" + '! + "{}"'.format(additional_text_new_pay), "PYTHON")
        
        arcpy.analysis.Split(base_data_path+"\Pay_torpaqi", base_data_path+"\Ev_Serheddi", 'Adi',newpay)
        
        arcpy.CalculateField_management(base_data_path+"\Ev_Serheddi", "Adi", '!Adi!.replace("{}", "")'.format(additional_text_new_pay), "PYTHON")
        
        
        ##################################### Kohne paylar #############################################
        arcpy.CalculateField_management(base_data_path+"\Ev_Serheddi", "Adi", '!' + "Adi" + '! + "{}"'.format(additional_text_old_pay), "PYTHON")
        
        arcpy.analysis.Split(base_data_path+"\Pay_Kohne", base_data_path+"\Ev_Serheddi", 'Adi',oldpay)
        
        arcpy.CalculateField_management(base_data_path+"\Ev_Serheddi", "Adi", '!Adi!.replace("{}", "")'.format(additional_text_old_pay), "PYTHON")
        
        ##################### check jn rn cn ################
        
        arcpy.env.workspace = newpay
        
        featureclasses = arcpy.ListFeatureClasses()
        
        for fc in featureclasses:
            newpayname.append(fc)
            
            newpayname.sort()
            
            arcpy.analysis.Statistics(fc,trash_data_path+"\Jn"+"{}".format(fc),[["Jn", "COUNT"]],"Jn")
            arcpy.analysis.Statistics(fc,trash_data_path+"\Rn"+"{}".format(fc),[["Rn", "COUNT"]],"Rn")
            arcpy.analysis.Statistics(fc,trash_data_path+"\Cn"+"{}".format(fc),[["Cn", "COUNT"]],"Cn")
            jn_summ = arcpy.management.SelectLayerByAttribute(trash_data_path+"\Jn"+"{}".format(fc), 'NEW_SELECTION',"COUNT_Jn = 2", 'NON_INVERT')
            Cn_summ = arcpy.management.SelectLayerByAttribute(trash_data_path+"\Cn"+"{}".format(fc), 'NEW_SELECTION',"COUNT_Cn = 2", 'NON_INVERT')
            Rn_summ = arcpy.management.SelectLayerByAttribute(trash_data_path+"\Rn"+"{}".format(fc), 'NEW_SELECTION',"COUNT_Rn = 2", 'NON_INVERT')
            
            count_jn_summ = arcpy.GetCount_management(jn_summ)
            count_rn_summ = arcpy.GetCount_management(Rn_summ)
            count_cn_summ = arcpy.GetCount_management(Cn_summ)
            
            if str(count_rn_summ) !="0":
                arcpy.conversion.ExportTable(Rn_summ,error_data_path+"\prn_tekrarlanir"+"_"+"{}".format(fc))
                
                
            if str(count_cn_summ) !="0":
                arcpy.conversion.ExportTable(Cn_summ,error_data_path+"\cn_tekrarlanir"+"_"+"{}".format(fc))
            
            
            if str(count_jn_summ) != "0":
                arcpy.conversion.ExportTable(jn_summ,error_data_path+"\jn_tekrarlanir"+"_"+"{}".format(fc))
                
                
                
        ####################################  join yeni kohne pay ###################################
        
        arcpy.env.workspace = oldpay
        featureclasses2 = arcpy.ListFeatureClasses()
        
        for fc2 in featureclasses2:
            
            oldpayname.append(fc2)
            oldpayname.sort()
            
            
        count_newpayname = len(newpayname)
        count_oldpayname = len(oldpayname)
        
        if count_newpayname == count_oldpayname:
            n=0
            while n < count_newpayname:
                print(newpay + "/" +str(newpayname[n]))
                arcpy.management.MakeFeatureLayer(newpay + "/" +str(newpayname[n]),newpayname[n]+str(n))
                arcpy.management.MakeFeatureLayer(oldpay + "/" +str(oldpayname[n]),oldpayname[n]+str(n))
                
                arcpy.management.AddJoin(newpayname[n]+str(n), 'Jn' , oldpayname[n]+str(n), 'Jn' , 'KEEP_ALL')
                
                
                selectshapeisnull = arcpy.management.SelectLayerByAttribute(newpayname[n]+str(n), 'NEW_SELECTION',"{}.SHAPE_Area IS NULL".format(oldpayname[n]), 'NON_INVERT')
                print("Sutun adi burda:","{}.SHAPE_Area IS NULL".format(oldpayname[n]))
                
                count_selectshapeisnull = arcpy.GetCount_management(selectshapeisnull)
                
                if str(count_selectshapeisnull)=="0":
                    arcpy.management.RemoveJoin(newpayname[n]+str(n),oldpayname[n])
                    
                if str(count_selectshapeisnull)!="0":         
                    arcpy.management.CopyFeatures(newpayname[n]+str(n),error_data_path+"\{}_Pay_Torpaqlari_Join_Edilmedi".format(newpayname[n]))
                    
                    arcpy.management.RemoveJoin(newpayname[n]+str(n),oldpayname[n])
                    
                    Rn_is_not_null = arcpy.management.SelectLayerByAttribute(newpayname[n]+str(n), 'NEW_SELECTION',"Rn IS NOT NULL", 'NON_INVERT')
                    
                    count_Rn_is_not_null = arcpy.GetCount_management(Rn_is_not_null)
                    
                    if str(count_Rn_is_not_null)!="0":
                        
                    
                        arcpy.management.AddJoin(newpayname[n]+str(n), 'Rn' , oldpayname[n]+str(n), 'Rn' , 'KEEP_ALL')
                    
                        selectrnisnull = arcpy.management.SelectLayerByAttribute(newpayname[n]+str(n), 'NEW_SELECTION',"{}.SHAPE_Area IS NOT NULL".format(oldpayname[n]), 'NON_INVERT')
                    
                        count_selectrnisnull = arcpy.GetCount_management(selectrnisnull)
                    
                        if str(count_selectrnisnull) !="0":
                            arcpy.management.CopyFeatures(newpayname[n]+str(n),trash_data_path+"\{}_Check_Pay_With_Rn".format(newpayname[n]))
                            

                            arcpy.management.MakeFeatureLayer(error_data_path+"\{}_Pay_Torpaqlari_Join_Edilmedi".format(newpayname[n]),"Pay_jn"+str(n))
                            arcpy.management.MakeFeatureLayer(trash_data_path+"\{}_Check_Pay_With_Rn".format(newpayname[n]),"Pay_rn"+str(n))
                            arcpy.management.SelectLayerByLocation("Pay_jn"+str(n), 'ARE_IDENTICAL_TO', "Pay_rn"+str(n))
                            arcpy.management.DeleteRows("Pay_jn"+str(n))
                            
                            end_count_feature = arcpy.GetCount_management("Pay_jn"+str(n))
                            
                            if str(end_count_feature) == "0":
                            
                                arcpy.management.Delete(error_data_path+"\{}_Pay_Torpaqlari_Join_Edilmedi".format(newpayname[n]))
                                
                                
                        arcpy.management.RemoveJoin(newpayname[n]+str(n),oldpayname[n])
                                
                        
                                
                                
                                
                arcpy.management.AddJoin(newpayname[n]+str(n), 'Jn' , oldpayname[n]+str(n), 'Jn' , 'KEEP_ALL')              
                selectshapeisNOTnull = arcpy.management.SelectLayerByAttribute(newpayname[n]+str(n), 'NEW_SELECTION',"{}.SHAPE_Area IS NOT NULL".format(oldpayname[n]), 'NON_INVERT')
                
                count_selectshapeisNOTnull = arcpy.GetCount_management(selectshapeisNOTnull)
                
                if str(count_selectshapeisNOTnull) !="0":
                    arcpy.management.CopyFeatures(newpayname[n]+str(n),trash_data_path+"\{}_shapeisNOTnull".format(newpayname[n]))
                    arcpy.management.MakeFeatureLayer(trash_data_path+"\{}_shapeisNOTnull".format(newpayname[n]),"isNotnull"+str(n))
                    
                    compare_Iha = arcpy.management.SelectLayerByAttribute("isNotnull"+str(n), 'NEW_SELECTION',"{}_I_Ha<>{}_I_HA".format(newpayname[n],oldpayname[n]), 'NON_INVERT')
                    
                    count_compare_Iha = arcpy.GetCount_management(compare_Iha)
                    
                    
                    if str(count_compare_Iha) !="0":
                        arcpy.management.CopyFeatures("isNotnull"+str(n),error_data_path+"\{}_Yeni_Paylarin_Iha_Kohne_pay_ile_eyni_deyil".format(newpayname[n]))
                        
                        
                arcpy.management.RemoveJoin(newpayname[n]+str(n),oldpayname[n])
                
                
                
                #### rn Iha compare ####
                selectrnisNOTnull = arcpy.management.SelectLayerByAttribute(newpayname[n]+str(n), 'NEW_SELECTION',"Rn IS NOT NULL", 'NON_INVERT')
                
                count_selectrnisNOTnull = arcpy.GetCount_management(selectrnisNOTnull)
                
                if str(count_selectrnisNOTnull) !="0":
                    arcpy.management.AddJoin(newpayname[n]+str(n), 'Rn' , oldpayname[n]+str(n), 'Rn' , 'KEEP_ALL')
                    selectShapeisNOTnull = arcpy.management.SelectLayerByAttribute(newpayname[n]+str(n), 'NEW_SELECTION',"{}.SHAPE_Area IS NOT NULL".format(oldpayname[n]), 'NON_INVERT')
                            
                    count_selectShapeisNOTnull = arcpy.GetCount_management(selectShapeisNOTnull)
                        
                    if str(count_selectShapeisNOTnull) !="0":
                        arcpy.management.CopyFeatures(newpayname[n]+str(n),trash_data_path+"\{}_Rncompare".format(newpayname[n]))
                        arcpy.management.MakeFeatureLayer(trash_data_path+"\{}_Rncompare".format(newpayname[n]),"RncompareisNotnull"+str(n))
                        
                        compare_Iha_rn = arcpy.management.SelectLayerByAttribute("RncompareisNotnull"+str(n), 'NEW_SELECTION',"{}_I_Ha<>{}_I_HA".format(newpayname[n],oldpayname[n]), 'NON_INVERT')
                        
                        count_compare_Iha_rn = arcpy.GetCount_management(compare_Iha_rn)
                        
                        if str(count_compare_Iha_rn) !="0":
                            arcpy.management.CopyFeatures("RncompareisNotnull"+str(n),error_data_path+"\{}_Rn_Join_Yeni_Paylarla_Kohne_Paylarin_I_ha_lari_ferqlidi".format(newpayname[n]))
                            
                    arcpy.management.RemoveJoin(newpayname[n]+str(n),oldpayname[n])
                    
                    
                
                
                
                
                    
                    
                Rn_is_not_null2 = arcpy.management.SelectLayerByAttribute(newpayname[n]+str(n), 'NEW_SELECTION',"Rn IS NOT NULL", 'NON_INVERT')
                    
                count_Rn_is_not_null2 = arcpy.GetCount_management(Rn_is_not_null2)
                    
                if str(count_Rn_is_not_null2)!="0":
                        
                    
                    arcpy.management.AddJoin(newpayname[n]+str(n), 'Rn' , oldpayname[n]+str(n), 'Rn' , 'KEEP_ALL')
                    
                    selectrnisnull2 = arcpy.management.SelectLayerByAttribute(newpayname[n]+str(n), 'NEW_SELECTION',"{}.SHAPE_Area IS NULL".format(oldpayname[n]), 'NON_INVERT')
                    
                    count_selectrnisnull2 = arcpy.GetCount_management(selectrnisnull2)
                    
                    if str(count_selectrnisnull2) =="0":
                        arcpy.management.RemoveJoin(newpayname[n]+str(n),oldpayname[n])
                    
                    if str(count_selectrnisnull2) !="0":
                        arcpy.management.CopyFeatures(newpayname[n]+str(n),error_data_path+"\{}_Pay_Torpaqlari_Join_Edilmedi_Rn".format(newpayname[n]))
                        
                        arcpy.management.RemoveJoin(newpayname[n]+str(n),oldpayname[n])
                        
                        
                        arcpy.management.AddJoin(newpayname[n]+str(n), 'Jn' , oldpayname[n]+str(n), 'Jn' , 'KEEP_ALL')
                        
                        selectjnisnull2 = arcpy.management.SelectLayerByAttribute(newpayname[n]+str(n), 'NEW_SELECTION',"{}.SHAPE_Area IS NOT NULL".format(oldpayname[n]), 'NON_INVERT')
                        
                        count_selectjnisnull2 = arcpy.GetCount_management(selectjnisnull2)
                        
                        if str(count_selectjnisnull2) =="0":
                            arcpy.management.RemoveJoin(newpayname[n]+str(n),oldpayname[n])
                            
                            
                        if str(count_selectjnisnull2) !="0":
                            arcpy.management.CopyFeatures(newpayname[n]+str(n),trash_data_path+"\{}_Check_Pay_With_Jn".format(newpayname[n]))
                            
                            arcpy.management.MakeFeatureLayer(trash_data_path+"\{}_Check_Pay_With_Jn".format(newpayname[n]),"Check_Pay_With_Jn_make"+str(n))
                            
                            arcpy.management.MakeFeatureLayer(error_data_path+"\{}_Pay_Torpaqlari_Join_Edilmedi_Rn".format(newpayname[n]),"Join_Edilmedi_Rn_make"+str(n))
                            
                            arcpy.management.RemoveJoin(newpayname[n]+str(n),oldpayname[n])
                            
                            arcpy.management.SelectLayerByLocation("Join_Edilmedi_Rn_make"+str(n), 'ARE_IDENTICAL_TO', "Check_Pay_With_Jn_make"+str(n))
                            
                            arcpy.management.DeleteRows("Join_Edilmedi_Rn_make"+str(n))
                            
                            arcpy.management.SelectLayerByAttribute("Join_Edilmedi_Rn_make"+str(n), 'CLEAR_SELECTION')
                            
                            end_count_feature2 = arcpy.GetCount_management("Join_Edilmedi_Rn_make"+str(n))
                            
                            if str(end_count_feature2) == "0":
                            
                                arcpy.management.Delete(error_data_path+"\{}_Pay_Torpaqlari_Join_Edilmedi_Rn".format(newpayname[n]))
                                
                            if str(end_count_feature2) != "0":
                
                                arcpy.management.MakeFeatureLayer(error_data_path+"\{}_Pay_Torpaqlari_Join_Edilmedi_Rn".format(newpayname[n]),"Join_Edilmedi_Rn_make_again"+str(n))
                                arcpy.management.MakeFeatureLayer(error_data_path+"\{}_Pay_Torpaqlari_Join_Edilmedi".format(newpayname[n]),"Join_Edilmedi_Jn_make_again"+str(n))            
                                                
                                arcpy.management.SelectLayerByLocation("Join_Edilmedi_Rn_make_again"+str(n), 'ARE_IDENTICAL_TO', "Join_Edilmedi_Jn_make_again"+str(n))
                                
                                arcpy.management.DeleteRows("Join_Edilmedi_Rn_make_again"+str(n))
                                
                                end_count_feature_rn = arcpy.GetCount_management("Join_Edilmedi_Rn_make_again"+str(n))
                                
                                if str(end_count_feature_rn) == "0":
                                    
                                    arcpy.management.Delete(error_data_path+"\{}_Pay_Torpaqlari_Join_Edilmedi_Rn".format(newpayname[n]))
                            
                        
                
                        
                    
                    
                    

                n+=1
                
        
        
                
                
            
            
            
        