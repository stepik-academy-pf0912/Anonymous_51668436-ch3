while True:
    # видео
    video_1_title = "First steps"
    video_1_link = "https://vk.com/timewebru?z=video150708314_456239286%2Fpl_wall_-28839208"
    video_2_title = "Work with text"
    video_2_link = "https://vk.com/timewebru?z=video150708314_456239287%2Fd99c47858502b4939a%2Fpl_wall_-28839208"
    video_3_title = "Lists on web-pages"
    video_3_link = "https://vk.com/timewebru?z=video150708314_456239288%2F36f31c3ea967903f44%2Fpl_wall_-28839208"
    video_4_title = "Blocks and tables"
    video_4_link = "https://vk.com/timewebru?z=video150708314_456239290%2F0dc4963a195e15d146%2Fpl_wall_-28839208"
    # плейлисты
    playlist_1_title = "Разметка текста"
    playlist_2_title = "Верстка"
    playlist_3_title = "Стилизация"



    print('Привет, это Stepik ***,  портал видео про язык HTML')
    print('Введите 1, чтобы посмотреть видео, 2 чтобы найти видео, 3 чтобы посмотреть плейлисты, exit или 0, чтобы выйти')

    playlists = [
    playlist_1_title, playlist_2_title, playlist_3_title
    ]

    videos = [
    video_1_title, video_2_title, video_3_title,video_4_title
    ]
    name = input()
    if name == '1':
        print('У нас нашлось 4 видео: ', *videos, sep='\n')
    elif name == '2':
        name_2 = input('Введите слово для поиска в видео: ')
        i = 0
        while i < len(videos):
            if name_2 in videos[i]:
                print('По этому слову есть: ', videos[i])
                i = i + 1
                break
    elif name == '3':
        print('У нас нашлось: ', *playlists, sep='\n')
        continue
    elif name == '0' or name == 'exit':
        break