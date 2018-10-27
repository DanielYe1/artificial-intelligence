/*Proposta de convenção: tudo que for proposta do candidato colocar no infinitivo, e tudo que ele afirma colocar no presente*/

investir(governo,ensinoMilitar).
investir(governo,pesquisa).
investir(governo,ensinoMedio).
investir(iniciativaPrivada,ensinoSuperior).
investir(governo,policiaMilitar).
investir(governo,turismo).

darPoder(policiaMilitar).
darPoder(policiaCivil).
darPoder(militares).

reformular(secretariaSeguranca).
reformular(sistemaPenitenciario).

combater(corrupcao).
combater(sonegacao).

causa(corrupcao, crise).
causa(sonegacao, crise).

reestruturar(administracaoPublica).

naoPriorizar(X, Y) :- setor(X), setor(Y).
/*Pensar em alguma forma de relacionar setor com serviço */
retiraDinheiro(corrupcao,X) :- servico(X),essencial(X).

sofre(estado,corrupcao).

deturpa(corrupcao, politicasPublicas).
retiraDinheiro(corrupcao, X) :- servicoEssencial(X).

estaAbandonado(saude).
estaAbandonado(educacao).
estaAbandonado(segurancaPublica).

desastre(UPP).
atrapalha(policiaParticular, planejamentoAtividadePolicial).
concorreInvestigacao(secretariaSegurancaPublica, policiaCivil).

extinguir(secretariaSegurancaPublica).
criar(secretariaPoliciaCivil).
criar(secretariaPoliciaMilitar).




