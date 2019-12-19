from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request
import os
import re

f = open('index.txt', 'r')
string_data = (f.read(200))
data = re.findall(r"[\w']+", string_data)
# Hence, data[0] = starting_month, data[1] =  starting_year, data[2] = ending_month, data[3]= ending_year

month_convert_num ={"january":"01","february":"02","march":"03","april":"04","may":"05","june":"06","july":"07","august":"08","september":"09","october":"10","november":"11","december":"12"}
month_convert_ascii = {1:"january",2:"february",3:"march",4:"april",5:"may",6:"june",7:"july",8:"august",9:"september",10:"october",11:"november",12:"december"}
os.makedirs("CnH Comics")

if(data[1]==data[3]):
    for month in range(int(month_convert_num[data[0]]), int(month_convert_num[data[2]])+1):
    
            source = requests.get('http://explosm.net/comics/archive/'+ str(data[1]) +'/' + str(month)).text

            soup = BeautifulSoup(source, 'lxml')

            comics = soup.find('div' , class_="small-7 medium-8 large-8 columns")

            os.makedirs("CnH Comics\\" + str(data[1]) +'\\'+ month_convert_ascii[month])

            for comic in comics.find_all('div', class_="small-12 medium-12 large-12 columns"):
                comic_num_src=comic.a['href']

                comic_data = comic.find('div', id="comic-author").text
                comic_date = comic_data[1:11]
                comic_author = comic_data.split(' ')[1]
                file_name = comic_date + '-' + comic_author + '.png'
                # print(file_name)

                comic_src_link = 'http://explosm.net' + comic_num_src
                
                comic_src_page = requests.get(comic_src_link).text
                comic_soup = BeautifulSoup(comic_src_page, 'lxml')
                
                comic_url_src = comic_soup.find('img', id="main-comic")
                comic_url = 'https://' + comic_url_src['src'][2:]
                # print(comic_url)

                if(comic_author.lower() == data[4].lower()):
                    comicfile = open("CnH Comics\\"+str(data[1])+"\\"+ month_convert_ascii[month]+"\\"+file_name, 'wb')
                    comicfile.write(urllib.request.urlopen(comic_url).read())
                    comicfile.close()


else :
    for year in range(int(data[1]), int(data[3])+1):

        if(year == int(data[1])) :
            for month in range(int(month_convert_num[data[0]]), 13):
        
                source = requests.get('http://explosm.net/comics/archive/'+ str(year) +'/' + str(month)).text

                soup = BeautifulSoup(source, 'lxml')

                comics = soup.find('div' , class_="small-7 medium-8 large-8 columns")

                os.makedirs("CnH Comics\\" + str(year) +'\\'+ month_convert_ascii[month])

                for comic in comics.find_all('div', class_="small-12 medium-12 large-12 columns"):
                    comic_num_src=comic.a['href']

                    comic_data = comic.find('div', id="comic-author").text
                    comic_date = comic_data[1:11]
                    comic_author = comic_data.split(' ')[1]
                    file_name = comic_date + '-' + comic_author + '.png'
                    # print(file_name)

                    comic_src_link = 'http://explosm.net' + comic_num_src
                    
                    comic_src_page = requests.get(comic_src_link).text
                    comic_soup = BeautifulSoup(comic_src_page, 'lxml')
                    
                    comic_url_src = comic_soup.find('img', id="main-comic")
                    comic_url = 'https://' + comic_url_src['src'][2:]
                    # print(comic_url)

                    if(comic_author.lower() == data[4].lower()):
                        comicfile = open("CnH Comics\\"+str(year)+"\\"+ month_convert_ascii[month]+"\\"+file_name, 'wb')
                        comicfile.write(urllib.request.urlopen(comic_url).read())
                        comicfile.close()
        
        elif(year == int(data[3])):
            for month in range(1, int(month_convert_num[data[2]])+1):
        
                source = requests.get('http://explosm.net/comics/archive/'+ str(year) +'/' + str(month)).text

                soup = BeautifulSoup(source, 'lxml')

                comics = soup.find('div' , class_="small-7 medium-8 large-8 columns")

                os.makedirs("CnH Comics\\" + str(year) +'\\'+ month_convert_ascii[month])

                for comic in comics.find_all('div', class_="small-12 medium-12 large-12 columns"):
                    comic_num_src=comic.a['href']

                    comic_data = comic.find('div', id="comic-author").text
                    comic_date = comic_data[1:11]
                    comic_author = comic_data.split(' ')[1]
                    file_name = comic_date + '-' + comic_author + '.png'
                    # print(file_name)

                    comic_src_link = 'http://explosm.net' + comic_num_src
                    
                    comic_src_page = requests.get(comic_src_link).text
                    comic_soup = BeautifulSoup(comic_src_page, 'lxml')
                    
                    comic_url_src = comic_soup.find('img', id="main-comic")
                    comic_url = 'https://' + comic_url_src['src'][2:]
                    # print(comic_url)

                    if(comic_author.lower() == data[4].lower()):
                        comicfile = open("CnH Comics\\"+str(year)+"\\"+ month_convert_ascii[month]+"\\"+file_name, 'wb')
                        comicfile.write(urllib.request.urlopen(comic_url).read())
                        comicfile.close()
                    
        else :
            for month in range(1, 13):
        
                source = requests.get('http://explosm.net/comics/archive/'+ str(year) +'/' + str(month)).text

                soup = BeautifulSoup(source, 'lxml')

                comics = soup.find('div' , class_="small-7 medium-8 large-8 columns")

                os.makedirs("CnH Comics\\" + str(year) +'\\'+ month_convert_ascii[month])

                for comic in comics.find_all('div', class_="small-12 medium-12 large-12 columns"):
                    comic_num_src=comic.a['href']

                    comic_data = comic.find('div', id="comic-author").text
                    comic_date = comic_data[1:11]
                    comic_author = comic_data.split(' ')[1]
                    file_name = comic_date + '-' + comic_author + '.png'
                    # print(file_name)

                    comic_src_link = 'http://explosm.net' + comic_num_src
                    
                    comic_src_page = requests.get(comic_src_link).text
                    comic_soup = BeautifulSoup(comic_src_page, 'lxml')
                    
                    comic_url_src = comic_soup.find('img', id="main-comic")
                    comic_url = 'https://' + comic_url_src['src'][2:]
                    # print(comic_url)

                    if(comic_author.lower() == data[4].lower()):
                        comicfile = open("CnH Comics\\"+str(year)+"\\"+month_convert_ascii[month]+"\\"+file_name, 'wb')
                        comicfile.write(urllib.request.urlopen(comic_url).read())
                        comicfile.close()



