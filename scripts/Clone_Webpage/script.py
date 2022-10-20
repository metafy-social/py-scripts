from pywebcopy import save_webpage

kwargs = {'project_name': 'site folder'}

save_webpage(

    # url of the website
    url='https://hacktoberfest.com/',

    # folder where the copy will be saved
    project_folder='Metafy-Scripts/Clone-a-webpage',
    **kwargs
)
