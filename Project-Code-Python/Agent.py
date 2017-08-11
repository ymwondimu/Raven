# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageChops, ImageOps
import numpy
import math

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        if len(problem.figures) == 9:
            return self.answer2x2(problem)
        else:
            if ( (problem.problemSetName == 'Basic Problems E') | (problem.problemSetName == 'Challenge Problems E') | (problem.problemSetName == 'Test Problems E') ):
                return self.answerSetE(problem)
            else:
                return self.answer3x3(problem)

    def answer3x3(self, problem):
        a = self.parseImage(problem, 'A')
        b = self.parseImage(problem, 'B')
        c = self.parseImage(problem, 'C')
        d = self.parseImage(problem, 'D')
        e = self.parseImage(problem, 'E')
        f = self.parseImage(problem, 'F')
        g = self.parseImage(problem, 'G')
        h = self.parseImage(problem, 'H')
        answer1 = self.parseImage(problem, '1')
        answer2 = self.parseImage(problem, '2')
        answer3 = self.parseImage(problem, '3')
        answer4 = self.parseImage(problem, '4')
        answer5 = self.parseImage(problem, '5')
        answer6 = self.parseImage(problem, '6')
        answer7 = self.parseImage(problem, '7')
        answer8 = self.parseImage(problem, '8')
        answerList = []
        answerList.append(['1', answer1])
        answerList.append(['2', answer2])
        answerList.append(['3', answer3])
        answerList.append(['4', answer4])
        answerList.append(['5', answer5])
        answerList.append(['6', answer6])
        answerList.append(['7', answer7])
        answerList.append(['8', answer8])
        ans_list = []

        ratioEF = self.getRatioImages(f, e)
        testRatio = self.getBlackPixelRatio(h) * ratioEF
        ans1 = self.findBestAnswerByBlackPixels(testRatio, answerList)
        ans1.append("EF")
        ans_list.append(ans1)

        """ratioEH = self.getRatioImages(h, e)
        testRatio2 = self.getBlackPixelRatio(f) * ratioEH
        ans2 = self.findBestAnswerByBlackPixels(testRatio2, answerList)
        ans2.append("EH")
        ans_list.append(ans2)

        ratioDG = self.getRatioImages(g, d)
        testRatio3 = self.getBlackPixelRatio(f) * ratioDG
        ans3 = self.findBestAnswerByBlackPixels(testRatio3, answerList)
        ans3.append("DG")
        ans_list.append(ans3)

        ratioAC = self.getRatioImages(c, a)
        testRatio4 = self.getBlackPixelRatio(g) * ratioAC
        ans4 = self.findBestAnswerByBlackPixels(testRatio4, answerList)
        ans4.append("AC")
        ans_list.append(ans4)

        ratioAE = self.getRatioImages(e, a)
        testRatio5 = self.getBlackPixelRatio(e) * ratioAE
        ans5 = self.findBestAnswerByBlackPixels(testRatio5, answerList)
        ans5.append("AE")
        ans_list.append(ans5)

        ratioDH = self.getRatioImages(h, d)
        testRatio6 = self.getBlackPixelRatio(e) * ratioDH
        ans6 = self.findBestAnswerByBlackPixels(testRatio6, answerList)
        ans6.append("DH")
        ans_list.append(ans6)
        if problem.name == 'Basic Problem D-06':
            print(ratioDH)
            print(testRatio6)
            print (testRatio)
            print(self.getBlackPixelRatio(e))
            print (self.compareRatio(testRatio6, answer1))
            print (self.compareRatio(testRatio, answer6))
            print(self.getBlackPixelRatio(answer1))
            print(self.getBlackPixelRatio(answer6))

        diffGH = self.getBlackPixels(h) - self.getBlackPixelRatio(g)
        test_blackPixels = self.getBlackPixels(h) + diffGH
        print (self.testBlackPixels(test_blackPixels, answerList))
        final_ans = self.bestAnswer(ans_list)"""

        ratioCD = self.getRatioImages(d, c)
        testRatio7 = self.getBlackPixelRatio(e) * ratioCD
        ans7 = self.findBestAnswerByBlackPixels(testRatio7, answerList)
        ans7.append("CD")
        ans_list.append(ans7)

        ans = self.bestAnswer(ans_list)



        transformList = []
        ABTransform = self.chooseTransform3x3(a, c, problem)
        ADTransform = self.chooseTransform3x3(a, g, problem)
        DiagTransform = self.chooseTransform3x3(a, e, problem)

        for transform in ABTransform:
            transformList.append(['AB', transform])
        for transform in ADTransform:
            transformList.append(['AD', transform])
        for transform in DiagTransform:
            transformList.append(['Diag', transform])

        test_metric = 0
        index = 0

        saveTransform = ""
        for i, transform in enumerate(transformList):
            if transform[0] == 'AB':
                test = self.performTransform(transform[1], g)
            elif transform[0] == 'Diag':
                test = self.performTransform(transform[1], e)
            else:
                test = self.performTransform(transform[1], c)

            test_heuristic = self.findBestAnswer(True, test, answerList)
            if test_heuristic[1] > test_metric:
                saveTransform = transform
                test_metric = test_heuristic[1]
                answerNum = test_heuristic[0]


        #print(problem.name)
        if test_metric > 0.9875:
            print(
                "Answer: " + str(answerNum) + ", Heuristic: " + str(test_metric) + ", Transform: " + str(saveTransform))
            return answerNum
        else:
            if ans[1] < 80:
                print ("-1")
                return -1
            else:
                print (ans)
                return ans[0]


    def answerSetE(self, problem):
        a = self.parseImage(problem, 'A')
        b = self.parseImage(problem, 'B')
        c = self.parseImage(problem, 'C')
        d = self.parseImage(problem, 'D')
        e = self.parseImage(problem, 'E')
        f = self.parseImage(problem, 'F')
        g = self.parseImage(problem, 'G')
        h = self.parseImage(problem, 'H')
        answer1 = self.parseImage(problem, '1')
        answer2 = self.parseImage(problem, '2')
        answer3 = self.parseImage(problem, '3')
        answer4 = self.parseImage(problem, '4')
        answer5 = self.parseImage(problem, '5')
        answer6 = self.parseImage(problem, '6')
        answer7 = self.parseImage(problem, '7')
        answer8 = self.parseImage(problem, '8')
        answerList = []
        answerList.append(['1', answer1])
        answerList.append(['2', answer2])
        answerList.append(['3', answer3])
        answerList.append(['4', answer4])
        answerList.append(['5', answer5])
        answerList.append(['6', answer6])
        answerList.append(['7', answer7])
        answerList.append(['8', answer8])
        #print (problem.name)

        transformList = []
        ABTransform = self.chooseTransformSetE(a, b, c)
        for transform in ABTransform:
            transformList.append(['AB', transform])

        test_metric = 0
        index = 0

        saveTransform = ""
        if len(transformList) == 0:
            return -1

        for i, transform in enumerate(transformList):
            if transform[0] == 'AB':
                test = self.performTransformSetE(transform[1], g, h)
            else:
                return -1

            test_heuristic = self.findBestAnswer(False, test, answerList)
            if test_heuristic[1] > test_metric:
                saveTransform = transform
                test_metric = test_heuristic[1]
                answerNum = test_heuristic[0]


        print ("Answer: " + str(answerNum) + ", Heuristic: " + str(test_metric) + ", Transform: " + str(saveTransform))
        if test_metric < 0.92:
            return -1
        else:
             # print (answerNum)
            return answerNum

    def answer2x2(self, problem):
        a = self.parseImage(problem, 'A')
        b = self.parseImage(problem, 'B')
        c = self.parseImage(problem, 'C')
        answer1 = self.parseImage(problem, '1')
        answer2 = self.parseImage(problem, '2')
        answer3 = self.parseImage(problem, '3')
        answer4 = self.parseImage(problem, '4')
        answer5 = self.parseImage(problem, '5')
        answer6 = self.parseImage(problem, '6')

        answerList = []
        answerList.append(['1', answer1])
        answerList.append(['2', answer2])
        answerList.append(['3', answer3])
        answerList.append(['4', answer4])
        answerList.append(['5', answer5])
        answerList.append(['6', answer6])
        #print(problem.name)

        transformList = []
        ABTransform = self.chooseTransform(a, b, problem)
        ACTransform = self.chooseTransform(a, c, problem)

        for transform in ABTransform:
            transformList.append(['AB', transform])
        for transform in ACTransform:
            if transform != 'Subtraction':
                transformList.append(['AC', transform])

        test_metric = 0
        index = 0

        saveTransform = ""
        for i, transform in enumerate(transformList):
            if transform[0] == 'AB':
                if transform[1] == 'Subtraction':
                    test = self.performSubtraction(a, b, c, problem)
                else:
                    test = self.performTransform(transform[1], c)
            else:
                test = self.performTransform(transform[1], b)

            test_heuristic = self.findBestAnswer(True, test, answerList)
            if test_heuristic[1] > test_metric:
                saveTransform = transform
                test_metric = test_heuristic[1]
                answerNum = test_heuristic[0]

        print ("Answer: " + str(answerNum) + ", Heuristic: " + str(test_metric) + ", Transform: " + str(saveTransform))
        if test_metric < 0.95:
            return -1
        else:
            print (answerNum)
            return answerNum

    def parseImage(self, problem, name):
        figure = problem.figures[name]
        im = Image.open(figure.visualFilename)

        return im

    def bestAnswer(self, answerList):
        max_val = 0
        index = 0
        for i, metric in enumerate(answerList):
            if metric[1] > max_val:
                max_val = metric[1]
                index = i

        return answerList[index]


    def performTransform(self, transform, image):
        if transform == 'Identity':
            return image
        elif transform == 'ReflectH':
            return self.reflectH(image)
        elif transform == 'Rot180':
            return self.rot180(image)
        elif transform == 'SwapLR':
            return self.swapLeftRight(image)
        else:
            return self.reflectV(image)

    def performTransformSetE(self, transform, image1, image2):
        if transform == 'FlipXOR':
            return self.flipXOR(image1, image2)
        elif transform == 'ImageOR':
            return self.ImageOR(image1, image2)
        else:
            return self.ImageXOR(image1, image2)

    def performSubtraction(self, image1, image2, image3, problem):
        array1 = numpy.asarray(image1)
        array2 = numpy.asarray(image2)
        array3 = numpy.asarray(image3)

        diffarray = numpy.subtract(array2, array1)
        final_array = numpy.add(diffarray, array3)

        img = Image.fromarray(final_array)
        return img

    def performAddition(self, image1, image2, image3, problem):
        array1 = numpy.asarray(image1)
        array2 = numpy.asarray(image2)
        array3 = numpy.asarray(image3)

        diffarray = numpy.subtract(array1, array2)
        final_array = numpy.subtract(array3, diffarray)

        img = Image.fromarray(final_array)
        return img

    def ImageXOR(self, image1, image2):
        array1 = self.convertNumpy(image1)
        array2 = self.convertNumpy(image2)

        final_array = numpy.logical_xor(array1, array2).astype(int)

        return final_array

    def flipXOR(self, image1, image2):
        image1_flipped = image1.transpose(Image.FLIP_LEFT_RIGHT)

        array1 = self.convertNumpy(image1_flipped)
        array2 = self.convertNumpy(image2)

        final_array = numpy.logical_xor(array1, array2).astype(int)
        return final_array



    def ImageOR(self, image1, image2):
        array1 = self.convertNumpy(image1)
        array2 = self.convertNumpy(image2)

        final_array = numpy.logical_or(array1, array2).astype(int)

        return final_array



    def findBestAnswer(self, image_bool, testImage, solutionList):
        equality_indicator = 0
        answerNum = -1
        """if image_bool == False:
            print (testImage)
            test = self.convertNumpy(testImage)
        else:
            test = testImage"""

        for i in range(len(solutionList)):
            if image_bool == False:
                temp = self.percentEqualArray(testImage, self.convertNumpy(solutionList[i][1]))
            else:
                temp = self.percentEqual(testImage, solutionList[i][1])
            if equality_indicator < temp:
                equality_indicator = temp
                answerNum = int(solutionList[i][0])

        return [answerNum, equality_indicator]

    def findBestAnswerByBlackPixels(self, testRatio, solutionList):
        equality_percent = 0
        answerNum = -1
        for i in range(len(solutionList)):
            temp = self.compareRatio(testRatio, solutionList[i][1])
            if equality_percent < temp:
                equality_percent = temp
                answerNum = int(solutionList[i][0])

        return [answerNum, equality_percent]


    def CCW90(self, image):
        image2 = image.rotate(90)
        return image2

    def CW90(self, image):
        image2 = image.rotate(-90)
        return image2

    def rot180(self, image):
        image2 = image.rotate(-180)
        return image2

    def reflectH(self, image):
        image2 = image.transpose(Image.FLIP_LEFT_RIGHT)
        return image2

    def reflectV(self, image):
        image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
        return image2

    def swapLeftRight(self, image):
        col, row = image.size
        pixels = image.load()

        for i in range(int(col/2)):
            for j in range(row):
                pixel1 = pixels[i, j]
                pixel2 = pixels[int(col/2)+i, j]
                pixels[i, j] = pixel2
                pixels[int(col/2)+i, j] = pixel1

        return image

    def swapLeftRight2(self, image):
        col, row = image.size
        pixels = image.load()
        quarter = int(col/4)
        half = int(col/2)
        three_quarter = int(3*(col/4))

        for i in range(quarter):
            for j in range(row):
                pixel1 = pixels[i, j]
                pixel2 = pixels[half-1-i, j]
                pixels[i, j] = pixel2
                pixels[half-1-i, j] = pixel1

        for x in range(half, three_quarter):
            for y in range(row):
                pixel3 = pixels[x, y]
                pixel4 = pixels[col-1-(x-half), y]
                pixels[x, y] = pixel4
                pixels[col-1-(x-half), y] = pixel3

        return image


    def convertNumpy(self, image):
        col, row = image.size
        data = numpy.zeros([row, col])

        pixels = image.load()
        for i in range(col):
            for j in range(row):
                pixel = pixels[i, j]
                if pixel[0] == 255:
                    data[i][j] = 0
                else:
                    data[i][j] = 1
        return data

    def subtractAndAdd(self, image1, image2, image3):
        intermediate_image = ImageChops.subtract(image2, image1)
        final_image = ImageChops.add(image3, intermediate_image)
        return final_image

    def addition(self, array1, array2):
        row, col = array1.shape

        temp = numpy.zeros([row, col])
        for i in range(row):
            for j in range(col):
                if array1[i][j] == 1 and array2[i][j] == 1:
                    temp[i][j] = 1
                else:
                    temp[i][j] = array1[i][j] + array2[i][j]

        return temp

    def percentEqual(self, image1, image2):
        array1 = self.convertNumpy(image1)
        array2 = self.convertNumpy(image2)

        row, col = array1.shape
        totalPixels = row*col
        equalPixels = 0

        for i in range(row):
            for j in range(col):
                args = (array1, array2, i, j)
                if self.matchLeft(*args) or self.matchRight(*args) or self.matchDown(*args) or self.matchUp(*args):
                    equalPixels+=1

        return equalPixels/totalPixels

    def percentEqualArray(self, array1, array2):
        row, col = array1.shape
        totalPixels = row * col
        equalPixels = 0

        for i in range(row):
            for j in range(col):
                args = (array1, array2, i, j)
                if self.matchLeft(*args) or self.matchRight(*args) or self.matchDown(*args) or self.matchUp(*args):
                    equalPixels += 1

        return equalPixels / totalPixels

    def getBlackPixelRatio(self, image1):
        array1 = self.convertNumpy(image1)

        row, col = array1.shape
        totalPixels = row*col
        blackPixels = 0

        for i in range(row):
            for j in range(col):
                if array1[i][j] == 1:
                    blackPixels += 1

        return blackPixels/totalPixels

    def getBlackPixels(self, image1):
        array1 = self.convertNumpy(image1)

        row, col = array1.shape
        totalPixels = row * col
        blackPixels = 0

        for i in range(row):
            for j in range(col):
                if array1[i][j] == 1:
                    blackPixels += 1

        return blackPixels

    def testBlackPixels(self, testNumBlack, solutionList):
        equality_percent = 0
        for i in range(len(solutionList)):
            blackPix = self.getBlackPixels((solutionList[i][1]))
            temp = abs(blackPix - testNumBlack)/(184*184)
            if equality_percent < temp:
                equality_percent = temp
                answerNum = int(solutionList[i][0])

        return [answerNum, equality_percent]

    def getRatioImages(self, image1, image2):
        ratio1 = self.getBlackPixelRatio(image1)
        ratio2 = self.getBlackPixelRatio(image2)

        return ratio1/ratio2

    def compareRatio(self, testRatio, image):
        image_ratio = self.getBlackPixelRatio(image)
        diff = abs(image_ratio-testRatio)/testRatio

        return 100-(diff*100)

    def matchLeft(self, array1, array2, x, y):
        return array1[x, y] == array2[x, max(0, y-1)]

    def matchRight(self, array1, array2, x, y):
        return array1[x, y] == array2[x, min(183, y+1)]

    def matchUp(self, array1, array2, x, y):
        return array1[x, y] == array2[max(0, x-1), y]

    def matchDown(self, array1, array2, x, y):
        return array1[x, y] == array2[min(183, x+1), y]

    def chooseTransform(self, image1, image2, problem):
        #clockwise90 = self.CW90(image1)
        #counter90 = self.CCW90(image1)
        reflectH = self.reflectH(image1)
        reflectV = self.reflectV(image1)
        identity = image1
        transform_list = []

        #clockwise90_equality = self.percentEqual(clockwise90, image2)
        #counter90_equality = self.percentEqual(counter90, image2)
        identity_equality = self.percentEqual(identity, image2)
        reflectH_equality = self.percentEqual(reflectH, image2)
        reflectV_equality = self.percentEqual(reflectV, image2)

        if identity_equality > 0.98:
            transform_list.append('Identity')
        if reflectH_equality > 0.98:
            transform_list.append('ReflectH')
        if reflectV_equality > 0.98:
            transform_list.append('ReflectV')

        transform_list.append('Subtraction')
        if len(problem.figures) != 9:
            transform_list.append('Addition')

        return transform_list

    def chooseTransform3x3(self, image1, image2, problem):
        reflectH = self.reflectH(image1)
        reflectV = self.reflectV(image1)
        rot180 = self.rot180(image1)
        swapLR = self.swapLeftRight(image1)
        identity = image1
        transform_list = []

        identity_equality = self.percentEqual(identity, image2)
        swapLR_equality = self.percentEqual(swapLR, image2)
        rot180_equality = self.percentEqual(rot180, image2)
        reflectH_equality = self.percentEqual(reflectH, image2)
        reflectV_equality = self.percentEqual(reflectV, image2)

        if identity_equality > 0.985:
            transform_list.append('Identity')
        if rot180_equality > 0.98:
            transform_list.append('Rot180')
        if reflectH_equality > 0.98:
            transform_list.append('ReflectH')
        if reflectV_equality > 0.98:
            transform_list.append('ReflectV')
        if swapLR_equality > 0.98:
            transform_list.append('SwapLR')

        return transform_list

    def chooseTransformSetE(self, image1, image2, image3):
        imageOR = self.ImageOR(image1, image2)
        imageXOR = self.ImageXOR(image1, image2)
        flipXOR = self.flipXOR(image1, image2)

        transform_list = []

        imageOR_equality = self.percentEqualArray(imageOR, self.convertNumpy(image3))
        imageXOR_equality = self.percentEqualArray(imageXOR, self.convertNumpy(image3))
        flipXOR_equality = self.percentEqualArray(flipXOR, self.convertNumpy(image3))

        #print ("OR: " + str(imageOR_equality))
        #print ("XOR: " + str(imageXOR_equality))
        #print ("FLIP: " + str(flipXOR_equality))

        if imageOR_equality > 0.98:
            transform_list.append('ImageOR')
        if imageXOR_equality > 0.98:
            transform_list.append('ImageXOR')
        #if flipXOR_equality > 0.98:
        #    transform_list.append('FlipXOR')
        #transform_list.append('ImageOR')
        #transform_list.append('ImageXOR')
        transform_list.append('FlipXOR')

        return transform_list