import string
import pandas as pd
import sys
import datetime 

# edit these for your own use.

org = "Phuong Hoang"
org_url="http://webhome.auburn.edu/~tzh0059/"
org_email="tzh0059@auburn.edu"

def extract_data(url):
    url_for_pandas = url.replace("/edit?usp=sharing", "/export?format=xlsx")
    df = pd.read_excel(url_for_pandas)
    return df

if __name__ == "__main__":
    if len(sys.argv) <= 3:
        print("Usage: python3 seminar_import.py <year> <semester> google_sheet_url")
        exit(1)
    print("Generating yml files for Hugo site...")
    print("Year: ", sys.argv[1])
    print("Semester: ", sys.argv[2])
    print("Google Sheet URL: ", sys.argv[3])

    df = extract_data(sys.argv[3])
    
    items_yml = open("data/items_"+ str(sys.argv[1]) + "_" + str(sys.argv[2]) + ".yml", "w")
    spotlights_yml = open("data/spotlights_"+ str(sys.argv[1]) + "_" + str(sys.argv[2]) + ".yml", "w")

    
    items_yml.write("title : \"Schedule "  +str(sys.argv[1])+" "+str(sys.argv[2]) + "\"\nid: \"schedule-"+str(sys.argv[1])+"-"+str(sys.argv[2])+"\"\ncontent: |\n "+"<b>For any questions or requests, please contact <a href="+str(org_url)+">"+str(org)+"</a>" + "(" + str(org_email) + ") </b>" + "\nstyle: \"style2 medium onscroll-fade-in\"\nitems:\n") 

    spotlights_yml.write("spotlights:\n")

    for index, row in df.iterrows():
    
        name     = row['Name']
        website  = row['Website']
        school   = row['School']
        date     = row['Date']
        time_loc = row['Time and Location']
        title    = row['Title']
        abstract = row['Abstract']
        image_url = row['Image URL']    

        # convert date string 
        date = datetime.datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S').strftime('%b %d')

        items_yml.write(" - name: " + "\"" + str(name) + "\"\n")
        items_yml.write("   website: " +  str(website) + "\n")
        items_yml.write("   school: " + "\"" + str(school) + "\"\n")
        items_yml.write("   date: " + "\"" + str(date) + " at " + str(time_loc) + "\"\n")
        items_yml.write("   link: " + "\"" + "#" + name.replace(" ", "") +"-" + str(sys.argv[1])+"-"+str(sys.argv[2]) + "\"\n")
        items_yml.write("   content: " + "\'" + str(title) + "\'\n")
        items_yml.write("   abstract: " +   str(abstract) + "\n")
        items_yml.write("   style: " + "\"solid style2 major fa-people-line\"\n\n\n")


        if index % 2 == 0:
            orient = "right"
        else:
            orient = "left"

        spotlights_yml.write("  - style: " + "\"style2 " + "orient-"+orient + " content-align-left" + " image-position-center" + " onscroll-image-fade-in\"\n")
        spotlights_yml.write("    id: " + "\"" + name.replace(" ", "") +"-" + str(sys.argv[1])+"-"+str(sys.argv[2]) + "\"\n")
        spotlights_yml.write("    title: " + "\"" + str(name) + "\"\n")
        spotlights_yml.write("    content: |\n" + "      " + str(title) + "\n")
        spotlights_yml.write("    abstract: " + str(abstract) + "\n")
        spotlights_yml.write("    image: \"" + str(image_url) + "\"\n\n\n")
    
    items_yml.close()
    spotlights_yml.close()