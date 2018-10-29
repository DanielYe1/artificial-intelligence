/* debate globo */
investir(iniciativaPrivada,presal).
investir(governo,ensinoTecnico).
investir(governo,escolasMilitares).

deveSer(municipio,responsavel,educacaoInfantil).

deveReceber(auxilio,iniciativaPrivada,saudePublica).

combater(trafico,auxilia,seguranca).
% bom senso
produz(pesquisa,ensinoTecnico).
produz(pesquisa,ensinoSuperior).
ehEnsino(ensinoTecnico).
ehEnsino(ensinoSuperior).
ehEnsino(escolasMilitares).
ehEnsino(escolasPublicas).


/* entrevista globo */

solucao(dividas,atrasoPagamento).
solucao(dividas,renegociacao).
solucao(dividas,recuperacaoFiscal).
solucao(dividas,capitalEstrangeiro).
solucao(dividas,aberturaDeCapital).

permitidaPor(capitalEstrangeiro,contratosDeLongoPrazo).
% bom senso
permitidaPor(renegociacao,pagamentoDeDebitos).
permitidaPor(renegociacao,corteDeCustos).
bloqueia(atrasoPagamento,pagamentoDeDebitos).


rever(congresso,recuperacaoFiscal).

extinguir(secretariaSegurancaPublica).
seraConduzida(seguranca,gabineteDeSeguranca).

iraConduzir(gabineteDeSeguranca,witzel).
iraConduzir(gabineteDeSeguranca,secretarioPoliciaMilitar).
iraConduzir(gabineteDeSeguranca,secretarioPoliciaCivil).

assistencia(qualquerPolicial,autoDeResistencia).

cobrar(universidadesPublicas).
manter(cotas).

/* polemicas sobre auxilioMoradia */
/*https://g1.globo.com/rj/rio-de-janeiro/eleicoes/2018/noticia/2018/10/28/wilson-witzel-do-psc-e-eleito-governador-do-rj.ghtml */
/* https://congressoemfoco.uol.com.br/especial/noticias/apenas-15-dos-juizes-federais-abrem-mao-de-auxilio-moradia-mostra-levantamento/ */
ehContra(auxilioMoradia,witzel).
ehContra(auxilioMoradia,carlosRoberto).
/* Fonte que era contra em junho: https://www1.folha.uol.com.br/poder/2018/06/pre-candidato-pelo-psc-ex-juiz-quer-extinguir-secretaria-de-seguranca-no-rj.shtml
 * Fonte que é a favor em outubro: https://www.bbc.com/portuguese/brasil-46013245 */
ehContra(politicaDeConfrontos, junho).
ehFavoravel(politicaDeAbates, outubro).
ehFavoravel(auxilioMoradia,luizFux).
recebe(auxilioMoradia,witzel).
recebe(auxilioMoradia,luizFux).


/* Prestar atenção a partir daqui, que foi onde realizei a primeira pergunta: ehSolucao(transformar(escolasPublicas, escolasMilitares))*/
proposta(transformar(escolasPublicas,escolasMilitares)).

/* Proposta para o que é uma solução de um problema político, geralmente podemos usar como template para uma pergunta,
 * ou seja, perguntamos à máquina ehSolucao(proposta) */
ehSolucao(X) :- proposta(X), X, melhora(vida, pessoas).

/* Senso comum 
 * Fonte para custos de escolas militares: https://politica.estadao.com.br/noticias/eleicoes,estudantes-de-colegio-militar-custam-tres-vezes-mais-ao-pais,70002473230
 * Fonte para falta de dinheiro do estado: https://g1.globo.com/rio-de-janeiro/noticia/rj-espera-deficit-de-r-10-bi-em-2018-metade-do-previsto-antes-do-regime-de-recuperacao-fiscal.ghtml
 * É senso comum de que é necessário investimento em áreas básicas como saúde, educação e transporte urbano */
falta(dinheiro, estado).
necessario(investimentos, areasBasicas).
transformar(escolasPublicas,escolasMilitares) :- multiplicaCusto(estudantes, 3).
melhora(vida, pessoas) :- not(cortaInvestimentos(areasBasicas)).
multiplicaCusto(estudantes, 3) :- not(falta(dinheiro, estado)) ; cortaInvestimentos(areasBasicas).
cortaInvestimentos(areasBasicas) :- not(necessario(investimentos, areasBasicas)).

/* fatos e regras para pergunta de discurso eleitoreiro */
equivalentes(politicaDeConfrontos,polit/* debate globo */
investir(iniciativaPrivada,presal).
investir(governo,ensinoTecnico).
investir(governo,escolasMilitares).

deveSer(municipio,responsavel,educacaoInfantil).

deveReceber(auxilio,iniciativaPrivada,saudePublica).

combater(trafico,auxilia,seguranca).
% bom senso
produz(pesquisa,ensinoTecnico).
produz(pesquisa,ensinoSuperior).
ehEnsino(ensinoTecnico).
ehEnsino(ensinoSuperior).
ehEnsino(escolasMilitares).
ehEnsino(escolasPublicas).


/* entrevista globo */

solucao(dividas,atrasoPagamento).
solucao(dividas,renegociacao).
solucao(dividas,recuperacaoFiscal).
solucao(dividas,capitalEstrangeiro).
solucao(dividas,aberturaDeCapital).

permitidaPor(capitalEstrangeiro,contratosDeLongoPrazo).
% bom senso
permitidaPor(renegociacao,pagamentoDeDebitos).
permitidaPor(renegociacao,corteDeCustos).
bloqueia(atrasoPagamento,pagamentoDeDebitos).


rever(congresso,recuperacaoFiscal).

extinguir(secretariaSegurancaPublica).
seraConduzida(seguranca,gabineteDeSeguranca).

iraConduzir(gabineteDeSeguranca,witzel).
iraConduzir(gabineteDeSeguranca,secretarioPoliciaMilitar).
iraConduzir(gabineteDeSeguranca,secretarioPoliciaCivil).

assistencia(qualquerPolicial,autoDeResistencia).

cobrar(universidadesPublicas).
manter(cotas).

/* polemicas sobre auxilioMoradia */
/*https://g1.globo.com/rj/rio-de-janeiro/eleicoes/2018/noticia/2018/10/28/wilson-witzel-do-psc-e-eleito-governador-do-rj.ghtml */
/* https://congressoemfoco.uol.com.br/especial/noticias/apenas-15-dos-juizes-federais-abrem-mao-de-auxilio-moradia-mostra-levantamento/ */
ehContra(auxilioMoradia,witzel).
ehContra(auxilioMoradia,carlosRoberto).
/* Fonte que era contra em junho: https://www1.folha.uol.com.br/poder/2018/06/pre-candidato-pelo-psc-ex-juiz-quer-extinguir-secretaria-de-seguranca-no-rj.shtml
 * Fonte que é a favor em outubro: https://www.bbc.com/portuguese/brasil-46013245 */
ehContra(politicaDeConfrontos, junho).
ehFavoravel(politicaDeAbates, outubro).
ehFavoravel(auxilioMoradia,luizFux).
recebe(auxilioMoradia,witzel).
recebe(auxilioMoradia,luizFux).


/* Prestar atenção a partir daqui, que foi onde realizei a primeira pergunta: ehSolucao(transformar(escolasPublicas, escolasMilitares))*/
proposta(transformar(escolasPublicas,escolasMilitares)).

/* Proposta para o que é uma solução de um problema político, geralmente podemos usar como template para uma pergunta,
 * ou seja, perguntamos à máquina ehSolucao(proposta) */
ehSolucao(X) :- proposta(X), X, melhora(vida, pessoas).

/* Senso comum 
 * Fonte para custos de escolas militares: https://politica.estadao.com.br/noticias/eleicoes,estudantes-de-colegio-militar-custam-tres-vezes-mais-ao-pais,70002473230
 * Fonte para falta de dinheiro do estado: https://g1.globo.com/rio-de-janeiro/noticia/rj-espera-deficit-de-r-10-bi-em-2018-metade-do-previsto-antes-do-regime-de-recuperacao-fiscal.ghtml
 * É senso comum de que é necessário investimento em áreas básicas como saúde, educação e transporte urbano */
falta(dinheiro, estado).
necessario(investimentos, areasBasicas).
transformar(escolasPublicas,escolasMilitares) :- multiplicaCusto(estudantes, 3).
melhora(vida, pessoas) :- not(cortaInvestimentos(areasBasicas)).
multiplicaCusto(estudantes, 3) :- not(falta(dinheiro, estado)) ; cortaInvestimentos(areasBasicas).
cortaInvestimentos(areasBasicas) :- not(necessario(investimentos, areasBasicas)).

/* fatos e regras para pergunta de discurso eleitoreiro */
equivalentes(politicaDeConfrontos,politicaDeAbates).
discursoEleitoreiro(X,Y) :- equivalentes(X, Y), ehContra(X, junho), ehFavoravel(Y, outubro).

/* fatos e regras para pergunta de combate à corrupção 
 * Fonte de proximidade com o operador do Cabral: https://www.oantagonista.com/brasil/proximidade-de-witzel-com-o-operador-de-cabral/
 * Fonte do combate à corrupção (seção 3.2 do plano de governo): http://divulgacandcontas.tse.jus.br/candidaturas/oficial/2018/BR/RJ/2022802018/190000612301/proposta_1534218285632.pdf*/
temProximidadeCom(aryFerreira).
condenado(aryFerreira, lavaJato).
querCombater(corrupcao, X) :- not(temProximidadeCom(X)), not(condenado(X, lavaJato)).

icaDeAbates).
discursoEleitoreiro(X,Y) :- equivalentes(X, Y), ehContra(X, junho), ehFavoravel(Y, outubro).

