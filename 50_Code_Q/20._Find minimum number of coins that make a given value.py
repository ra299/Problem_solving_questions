import sys

def minCoin(coins, len_ofCoins, V):

    if(
        V <= 0
    ) : return 0
    res = sys.maxsize

    for i in range(0, len_ofCoins):
        if(coins[i] <= V):
            sub_res = minCoin(coins, len_ofCoins, V- coins[i])

            if (sub_res != sys.maxsize and sub_res + 1 < res): 
                res = sub_res +1

    return res


if __name__ == "__main__":
    coins = [9,6,5,1]
    len_ofCoins = len(coins)
    V = 11

    print("Total Coins required-->", minCoin(coins, len_ofCoins, V))