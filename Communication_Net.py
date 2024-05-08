import arcpy

class Netwrok:
    def __init__(self,base_data_path,azcad_data_base,checkbox_value,textBrowser,readme,head):
        super().__init__()
        base_data_path = base_data_path +'\RAYON'
        self.network_append(base_data_path,azcad_data_base,checkbox_value,textBrowser,readme,head)
        
        
    def network_append(self,base_data_path,azcad_data_base,checkbox_value,textBrowser,readme,head):
        
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        
        try:
        
            arcpy.management.Append(base_data_path+'\HATLAR', azcad_data_base+'\COMMUNICATION_NETWORK', 'NO_TEST')
            if checkbox_value:
                readme.write("\n")
                readme.write("\n36. Kommunikasiya xetleri bagli prosesler hell edildi")
            cursor.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')
            cursor.insertHtml('''<p><span style="color:green;">Kommunikasiya xətləri ilə bağlı proseslər həll edildi <br> </span>''')
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n36. Kommunikasiya xetleri ile bagli prosesde xeta bas verdi. Araliq bazada hatlar layinin movcud oldugundan emin olun!")
            cursor.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------------</strong><br> </span>''')
            cursor.insertHtml('''<p><span style="color:red;">Kommunikasiya xətləri ilə bağlı proseslərdə xəta baş verdi. Aralıq bazada Hatlar layının mövcud
                              olduğundan əmin olun!<br> </span>''')
            
        if checkbox_value:    
            readme.close()