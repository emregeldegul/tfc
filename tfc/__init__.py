from .tfc import Translation

def main():
    print('TFC listens To Your Clipboard For Translation.')
    print('='*50)

    translation = Translation()
    translation.start()

if __name__ == '__main__':
    main()
