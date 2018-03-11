import pygame,os,random,tkinter

root = tkinter.Tk()
root.title("BubbleSort")
root.resizable(width=False, height=False)
root.minsize(width=1280, height=720)
root.maxsize(width=1280, height=720)
embed = tkinter.Frame(root, width=1280, height=720)
embed.grid(columnspan=(600), rowspan=500)
embed.pack(side=tkinter.TOP)
buttonwin = tkinter.Frame(root, width=100, height=500)
buttonwin.pack(side=tkinter.LEFT)
root.configure(background="white")
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()
pygame.font.init()
pygame.mixer.init()
infoFont = pygame.font.SysFont("Arial", 24, italic=True)
scr_w, scr_h = 1280, 720
screen = pygame.display.set_mode((scr_w, scr_h))
#mode = input("Mode? (Automatic(A) or Manual(M))")
root.lift()


def GenerateList():
    global genMax,genLen, bubsortWidth, bubsortHeight,spaceWidth
    spaceWidth = 5  # Pixels
    for x in open("config.txt").readlines():
        if "genLen:" in x:
            genLen = int(x.replace("genLen:","").replace('\n',''))
        elif "genMax" in x:
            genMax = int(x.replace("genMax:","").replace('\n',''))
    genList = []
    for x in range(0, genLen):
        genList.append(random.randint(0, genMax))
    lenList = len(genList)
    spaceAmnt = lenList + 1
    bubsortWidth = ((1280 - (spaceWidth * spaceAmnt)) / lenList)
    bubsortHeight = (scr_h / genMax)
    return genList

def BubbleSort(unsortedList):
    for i, v in enumerate(unsortedList):
        try:
            if (v > unsortedList[i + 1]):
                unsortedList[i] = unsortedList[i + 1]
                unsortedList[i + 1] = v
            else:
                pass
        except IndexError:
            pass
    return unsortedList


def CheckSorted(listToCheck):
    try:
        for i, v in enumerate(listToCheck):
            if (v > listToCheck[i + 1]):
                return False
            else:
                pass
    except IndexError:
        return True


def PyMain():
    global scr_h,scr_w,lenList,bubXval
    bubXval = 0
    logo = pygame.image.load('logo.png')
    finishedSound = pygame.mixer.Sound("finsound.wav")
    finishedSound.set_volume(1)
    lineWidth = 2
    genList = GenerateList()
    loopAmnt = 1
    allowNext = True
    screen.fill((225, 225, 225))
    screen.blit(logo, (5, 90))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    allowNext = True
                    genList = GenerateList()
                    Bub = BubbleSort(genList)
                if allowNext:
                    screen.fill((225, 225, 225))
                    screen.blit(logo, (5, 90))
                    Bub = BubbleSort(genList)
                    color = (random.randint(30, 255), random.randint(30, 255), random.randint(30, 255))
                    for eachNum in Bub:
                        pygame.draw.rect(screen, color,
                                         (bubXval, 715, bubsortWidth, -(eachNum * bubsortHeight) + 10))
                        pygame.draw.rect(screen, (0, 0, 0),
                                         (bubXval, 715, bubsortWidth, -(eachNum * bubsortHeight) + 10), lineWidth)
                        bubXval += bubsortWidth + spaceWidth
                        # print(bubXval)
                    bubXval = 0
                    loopAmnt += 1
                    print(Bub)
                    if (CheckSorted(Bub)):
                        finishedSound.play()
                        allowNext = False
                        print("#########################################################")
                        print("FINISHED BUBBLESORTING")
                        print("This took: " + str(loopAmnt) + " loops to sort")
                        print("#########################################################")
                        loopAmnt = 0
                        genList = GenerateList()

                    # screen.fill((225, 225, 225))

            elif event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(infoFont.render("Press any key (besides enter) to perform a loop of bubblesorting.", False, (0, 0, 0)), (0, 0))
        screen.blit(infoFont.render("Press Enter to generate new values.", False, (0, 0, 0)), (0, 25))
        screen.blit(infoFont.render("See config.txt for configurable settings (you can change values and stuff)", False,
                                    (0, 0, 0)), (0, 50))
        screen.blit(infoFont.render("Program may not respond when trying to sort through a large amount of numbers, as bubblesort is not very efficient.", False,
                                    (0, 0, 0)), (0, 75))
        try:
            root.update()
            pygame.display.update()
        except:
            print("App closed.")

if __name__ == "__main__":
    PyMain()
