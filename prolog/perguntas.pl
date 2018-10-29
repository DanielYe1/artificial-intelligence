% p1
ehSolucao(transformar(escolasPublicas, escolasMilitares)).

%p2 
ehContra(X,Y),recebe(X,Y).

%p3 verifica solucoes,verifica o que permite as solucoes, verifica se alguma solucao bloqueia a resolucao de outra
solucao(A,B),solucao(X,Y),permitidaPor(Y,Z),bloqueia(B,Z).