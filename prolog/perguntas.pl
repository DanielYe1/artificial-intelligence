%p1 transformar escolas públicas em militares é uma solução viável?
ehSolucao(transformar(escolasPublicas, escolasMilitares)).

%p2 
ehContra(X,Y),recebe(X,Y).

%p3 verifica solucoes,verifica o que permite as solucoes, verifica se alguma solucao bloqueia a resolucao de outra
solucao(A,B),solucao(X,Y),permitidaPor(Y,Z),bloqueia(B,Z).

%p4 existe alguma instituicao de ensino que o governo investe que produz coisas pra iniciativaPrivada e vice versa?
investir(governo,X),investir(iniciativaPrivada,Y),((ehEnsino(X),produz(Y,X));(ehEnsino(Y),(produz(X,Y)))).

%p5 intervenção militar foi positiva no rio e deixa um legado para a segurança pública
intervencao(X,Y) ; positivo(X,Y)

%p6 o discurso de política de confrontos é eleitoreiro, ou seja, ele propunha algo antes e mudou o discurso em poucos meses?
discursoEleitoreiro(politicaDeConfrontos, politicaDeAbates)

%p7 o candidato quer de fato combater a corrupção?
querCombater(corrupcao, aryFerreira)

%p8 Witzel pode ser considerado um corruptor?
corruptor(witzel)