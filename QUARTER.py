import arcpy


class Quarter:
    def __init__(self,base_data_path,azcad_data_base,output_data_path,checkbox_value,textBrowser,readme,head):
        super().__init__()
        self.quarter_append(base_data_path,azcad_data_base,output_data_path,checkbox_value,textBrowser,readme,head)
        
        
    def quarter_append(self,base_data_path,azcad_data_base,output_data_path,checkbox_value,textBrowser,readme,head):
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        
        try:
            arcpy.management.Append(base_data_path+'\QUARTER', azcad_data_base+'\QUARTER', 'NO_TEST')
            
            ############## newww ############            
            arcpy.management.MakeFeatureLayer(azcad_data_base+'\OCCUPATION',"make_quarter")
            
            arcpy.management.CalculateField("make_quarter", 'TOTAL_AREA','round(!SHAPE_Area!,0)')
            ############## newww ############  

            arcpy.analysis.Intersect([azcad_data_base+'\OCCUPATION',base_data_path+'\QUARTER'],output_data_path+'\Quarter_Occup', 'ALL')
            
            arcpy.management.MakeFeatureLayer(azcad_data_base+'\OCCUPATION',"make_occu")
            
            arcpy.management.MakeFeatureLayer(output_data_path+'\Quarter_Occup',"make_quart_occu")
            
            arcpy.management.AddJoin('make_occu', 'OBJECTID', 'make_quart_occu', 'FID_OCCUPATION', 'KEEP_ALL')
            
            arcpy.management.CalculateField("make_occu", 'OCCUPATION.FK_QUARTER','!Quarter_Occup.FID_QUARTER!')
            
            
            arcpy.management.RemoveJoin('make_occu', 'Quarter_Occup')
            
            
            
            
            ############################### Quarter Parcel relation ########################################
            arcpy.analysis.Intersect([azcad_data_base+'\PARCEL',azcad_data_base+'\QUARTER'],output_data_path+'\Quarter_Parcel1', 'ALL')
            
            arcpy.management.MakeFeatureLayer(azcad_data_base+'\PARCEL',"make_p")
            
            arcpy.management.MakeFeatureLayer(output_data_path+'\Quarter_Parcel1',"q_p1")
            
            arcpy.management.AddJoin('make_p', 'OBJECTID', 'q_p1', 'FID_PARCEL', 'KEEP_ALL')
            
            arcpy.management.CalculateField("make_p", 'PARCEL.FK_QUARTER','!Quarter_Parcel1.FID_QUARTER!')
            
            arcpy.management.RemoveJoin('make_p', 'Quarter_Parcel1')
            

            ############################### Quarter Parcel relation ########################################
            
            ############################### Quarter Sector relation ########################################
            arcpy.analysis.Intersect([azcad_data_base+'\QUARTER',azcad_data_base+'\SECTOR'],output_data_path+'\Quarter_Sector1', 'ALL')
            
            arcpy.management.MakeFeatureLayer(azcad_data_base+'\QUARTER',"qu1")
            
            arcpy.management.MakeFeatureLayer(output_data_path+'\Quarter_Sector1',"qu_s1")
            
            arcpy.management.AddJoin('qu1', 'OBJECTID', 'qu_s1', 'FID_QUARTER', 'KEEP_ALL')
            
            arcpy.management.CalculateField("qu1", 'QUARTER.FK_SECTOR','!Quarter_Sector1.FID_SECTOR!')
            
            arcpy.management.RemoveJoin('qu1', 'Quarter_Sector1')
            ############################### Quarter Sector relation ########################################
            
            if checkbox_value:
                readme.write("\n")
                readme.write("\n35. Quarter ile bagli butun prosesler hell edildi (Quarter sector relation, Quarter parcel relation)")
            cursor.insertHtml('''<p><span style="color:green;">Quarter ilə bağlı bütün proseslər həll edildi(Quarter sector relation, Quarter parcel relation) <br> </span>''')
            
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n35. Quarter ile bagli proseslerde xeta bas verdi. Araliq bazada Quarter layinin oldugundan emin olun!")
            cursor.insertHtml('''<p><span style="color:red;">Quarter ilə bağlı proseslərdə xəta baş verdi. Aralıq bazada Quarter layının olduğundan əmin olun! <br> </span>''')
            
            
        if checkbox_value:    
            readme.close()