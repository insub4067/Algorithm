# 피타고라스 정리
print("-- 피타고라스 정리 계산기 --")

ytox = input("조건 1 : y에서 x까지의 거리는?\n")
ytoz = input(("조건 2 : y에서 z까지의 거리는?\n"))
answer_square = eval("int(ytox) ** 2 + int(ytoz) ** 2")
print("정답 : ", end="")
print(eval("answer_square ** (1/2)"))
