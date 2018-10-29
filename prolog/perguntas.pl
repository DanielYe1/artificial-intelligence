% p1
ehSolucao(transformar(escolasPublicas, escolasMilitares)).

%p2
ehContra(X,Y),recebe(X,Y).

%p3
solucao(A,B),solucao(X,Y),permitidaPor(Y,Z),bloqueia(B,Z).