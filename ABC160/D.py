def main():
    N, X, Y = map(int, input().split())

    G = []
    for i in range(1,N):
        if i == X:
            G.append([i+1,Y])
        else:
            G.append(i+1)

    print(G)

    distance = {i:1 for i in range(1,N+1)}
    for i in range(N-1):
        if i+1 != X and i < N:
          distance[G[i]+1] += distance[G[i]]
        else:
            pass
        print(G[i])

    print(distance)

    # for i in range(N-1):
    #     print(distance[i])

if __name__ == '__main__':
    main()