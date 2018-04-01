from analyse_tags import Tags

if __name__ == '__main__':
    print('jello')
    tags = Tags()
    for tag in tags.keys:
        print(tag)
    while True:
        tag_input = raw_input() 
        print('for tag: ', tag_input )
        print(tags.getTagData([tag_input]))
