import random

ZUKOWSKA = [
    [
    ],
    [
    ],
    [
    ],
    [
    ],
    [
    ],
    [
    ]
]


def zukowska_random():
    answer = [random.choice(ZUKOWSKA[i]) for i in range(len(ZUKOWSKA))]
    return " ".join(answer)


if __name__ == "__main__":
    print(zukowska_random())
