import random
import tkinter.messagebox as msgbox
import tkinter as tk
import colors as cl
class Game:
    def __init__(self, master):
        self.size = 4
        self.main_window = master
        self.cv = tk.Canvas(self.main_window, width = 500, height = 500, bg = cl.BACKGROUND)
        for i in range(0, 4):
            for j in range(0, 4):
                self.cv.create_rectangle(20 + 120 * j, 20 + 120 * i, 120 + 120 * j, 120 + 120 * i)

        self.color_map = cl.COLOR_MAP
        self.rectangles = []
        for i in range(0, 4):
            row = []
            for j in range(0, 4):
                rect = self.cv.create_rectangle(
                    20 + 120 * j, 20 + 120 * i, 
                    120 + 120 * j, 120 + 120 * i,
                    fill=self.color_map.get(0), outline=self.color_map.get(0), width=2
                )
                row.append(rect)
            self.rectangles.append(row)
        self.cv.pack()
        self.bind_keys()
        self.numbers = []
        self.matrix = self.creat()
    def display(self, matrix):
        for item in self.numbers:
            self.cv.delete(item)
        self.numbers.clear()
        for i in range(4):
            for j in range(4):
                text_color = cl.TEXT_DARK if matrix[i][j] in [2, 4] else cl.TEXT_LIGHT
                color = self.color_map.get(matrix[i][j], cl.DEFAULT_COLOR)
                self.cv.itemconfig(self.rectangles[i][j], fill=color)
                if matrix[i][j] != 0:
                    cvNumbers = self.cv.create_text(
                        70 + 120 * j, 70 + 120 * i, 
                        text=matrix[i][j], 
                        font=("Arial", 35, "bold"),
                        fill = text_color
                    )
                    self.numbers.append(cvNumbers)
    def bind_keys(self):
        self.main_window.bind("<Up>", lambda act: self.moveUp(self.matrix))
        self.main_window.bind("<Down>", lambda act: self.moveDown(self.matrix))
        self.main_window.bind("<Left>", lambda act: self.moveLeft(self.matrix))
        self.main_window.bind("<Right>", lambda act: self.moveRight(self.matrix))
    def creat(self):
        matrix = [[0 for i in range(self.size)] for i in range(self.size)]
        for i in range(2):
            matrix = self.newNum(matrix)
        self.display(matrix)
        self.matrix = matrix
        return matrix
    def getEmpty(self, matrix):
        list = []
        for i in range(self.size):
            for j in range(self.size):
                if matrix[i][j] == 0:
                    list.append([i, j])
        return list
    def randomPlace(self, matrix):
        empty = self.getEmpty(matrix)
        place = random.randint(0, len(empty) - 1)
        return empty[place]
    def randomNum(self, matrix):
        num = random.randint(1, 10)
        if(num < 10): num = 2
        else: num = 4
        place = self.randomPlace(matrix)
        return place, num
    def newNum(self, matrix):
        randomNum = self.randomNum(matrix)
        numPlace = randomNum[0]
        num = randomNum[1]
        matrix[numPlace[0]][numPlace[1]] = num
        return matrix
    def moveUp(self, matrix):
        old = [i[:] for i in matrix]
        for j in range(self.size):
            index = 0
            for i in range(1, self.size):
                if(matrix[i][j] != 0):
                    if(matrix[index][j] == matrix[i][j]):
                        matrix[index][j] += matrix[i][j]
                        matrix[i][j] = 0
                        index += 1
                    elif(matrix[index][j] == 0):
                        matrix[index][j] = matrix[i][j]
                        matrix[i][j] = 0
                    else:
                        index += 1
                        if(matrix[index][j] == 0):
                            matrix[index][j] = matrix[i][j]
                            matrix[i][j] = 0
        if(matrix != old):
            matrix = self.newNum(matrix)
            self.display(matrix)
            self.matrix = matrix
            self.game_over()
            return matrix
        else: return old
    def moveDown(self, matrix):
        old = [i[:] for i in matrix]
        for j in range(self.size):
            index = 3
            for i in range(self.size - 2, -1, -1):
                if(matrix[i][j] != 0):
                    if(matrix[index][j] == matrix[i][j]):
                        matrix[index][j] += matrix[i][j]
                        matrix[i][j] = 0
                        index -= 1
                    elif(matrix[index][j] == 0):
                        matrix[index][j] = matrix[i][j]
                        matrix[i][j] = 0
                    else:
                        index -= 1
                        if(matrix[index][j] == 0):
                            matrix[index][j] = matrix[i][j]
                            matrix[i][j] = 0
        if(matrix != old):
            matrix = self.newNum(matrix)
            self.display(matrix)
            self.matrix = matrix
            self.game_over()
            return matrix
        else: return old
    def moveLeft(self, matrix):
        old = [i[:] for i in matrix]
        for i in range(self.size):
            index = 0
            for j in range(1, self.size):
                if(matrix[i][j] != 0):
                    if(matrix[i][index] == matrix[i][j]):
                        matrix[i][index] += matrix[i][j]
                        matrix[i][j] = 0
                        index += 1
                    elif(matrix[i][index] == 0):
                        matrix[i][index] = matrix[i][j]
                        matrix[i][j] = 0
                    else:
                        index += 1
                        if(matrix[i][index] == 0):
                            matrix[i][index] = matrix[i][j]
                            matrix[i][j] = 0
        if(matrix != old):
            matrix = self.newNum(matrix)
            self.display(matrix)
            self.matrix = matrix
            self.game_over()
            return matrix
        else: return old
    def moveRight(self, matrix):
        old = [i[:] for i in matrix]
        for i in range(self.size):
            index = 3
            for j in range(self.size - 2, -1, -1):
                if(matrix[i][j] != 0):
                    if(matrix[i][index] == matrix[i][j]):
                        matrix[i][index] += matrix[i][j]
                        matrix[i][j] = 0
                        index -= 1
                    elif(matrix[i][index] == 0):
                        matrix[i][index] = matrix[i][j]
                        matrix[i][j] = 0
                    else:
                        index -= 1
                        if(matrix[i][index] == 0):
                            matrix[i][index] = matrix[i][j]
                            matrix[i][j] = 0
        if(matrix != old):
            matrix = self.newNum(matrix)
            self.display(matrix)
            self.matrix = matrix
            self.game_over()
            return matrix
        else: return old

    def game_over(self):
         for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 2048:
                    msgbox.showinfo("Game End", "You win!")
                    return True
         for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    return False
         for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j+1]:
                    return False
         for j in range(4):
            for i in range(3):
                if self.matrix[i][j] == self.matrix[i+1][j]:
                    return False
         msgbox.showinfo("Game Over!","Exit")
         return True
                        
root = tk.Tk()
game = Game(root)
root.mainloop()
