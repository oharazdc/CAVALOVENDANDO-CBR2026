# Guia mestre - RCB Challenge 2026 e autonomia do robô

**Uso:** referência duradoura para equipe, manutenção do código e agentes/chats futuros.  
**Regulamento-base:** *Regras Challenge 2026 Português, versão 1.0*, 12 páginas, fornecido pela equipe.  
**Atualizado em:** 23/10/2026.  
**Escopo do hardware descrito:** projeto `CAVALOVENDANDO-CBR2026`, dois hubs Pybricks.

> Este guia distingue requisitos publicados pela competição de orientações de projeto e fatos ainda não verificados. Se uma versão posterior do regulamento, a organização ou o árbitro divergir deste resumo, prevalece a decisão oficial mais recente. Não transforme uma hipótese de estratégia em regra oficial.

## 1. Intenção do desafio

Construir e programar um robô que, sem controle humano durante a partida, se localize e se mova pela arena, reconheça cubos recicláveis, recolha os cubos elegíveis, transporte cada um até a plataforma da cor correspondente e evite obstáculos, limites e o robô adversário. O objetivo de pontuação é concluir o maior número de entregas válidas dentro do tempo.

O robô deve decidir a partir de sensores embarcados. Não pode depender de câmera, LiDAR ou processamento de imagem: esses meios são expressamente proibidos. Os sensores permitidos não garantem que toda situação possa ser identificada com certeza; quando a leitura for ambígua, o comportamento seguro é parar ou recuar, manter o objeto intacto e escolher caminho alternativo em vez de empurrar ou coletar às cegas.

## 2. Autoridade e natureza das informações

- **Regra oficial:** requisito ou pontuação descrita no regulamento v1.0.
- **Estado do projeto:** ligação de hardware, calibração ou capacidade observável nos arquivos atuais.
- **Diretriz de autonomia:** comportamento recomendado para cumprir as regras. Não é texto oficial nem garante pontuação automática.
- **A confirmar:** dado que depende da arena real, inspeção do robô, calibração, organizadores ou versão futura do regulamento.

Este guia é um resumo operacional, não substitui as 12 páginas do regulamento nem parecer do árbitro. Ele documenta o objetivo; não afirma que o firmware atual já o implementa. O código do projeto ainda é inicial/prova de conceito e **não está pronto para uma partida autônoma completa**.

## 3. Arena: dimensões, zonas, linhas e posições

A pista total mede **2840 × 1500 mm**, é impressa em lona e tem lados espelhados. A equipe começa em uma das metades e nunca deve atravessar para a área livre (verde) da outra equipe.

| Elemento | Aparência / dimensão do regulamento | O que significa para o robô |
|---|---|---|
| Ecoponto | Amarelo, **220 × 1460 mm**, em cada extremidade | Zona de destino. O robô da equipe pode circular nela. Entrar no amarelo não é infração. Localizar a marca/plataforma correta e descarregar sem deslocá-la. |
| Área livre | Verde, **280 × 1460 mm**, entre Ecoponto e cidade | Zona de início e circulação exclusiva da equipe daquele lado. O robô inicia em posição aleatória nessa área, posta pelo árbitro. Cubo largado integralmente nessa zona pode se enquadrar na regra de não perdido; a tentativa de pontuação válida, porém, exige plataforma correspondente. |
| Cidade / ruas | Fundo claro; ruas marcadas por linhas pretas de **20 mm** | Zona de coleta. As linhas pretas representam vias e devem ser seguidas consistentemente. Quadrados cinza sobre elas indicam pontos possíveis de cubos coloridos. |
| Linha azul | **20 mm**, fronteira entre área livre e cidade | Referência de entrada/limite de lado. Não cruzar a linha azul do lado oposto nem ocupar a área verde adversária; isso caracteriza robô perdido. Ao sair da própria área permitida, há penalidade. |
| Linha vermelha | **20 mm**, limites exteriores da cidade | Barreira rígida de segurança. Qualquer sensor de chão que detecte vermelho deve interromper imediatamente o avanço para esse limite e iniciar recuperação para dentro da pista. Cruzar/sair da área acarreta penalidade e reposicionamento. |
| Quadrados brancos dentro do amarelo | Cinco retângulos de **160 × 50 mm** por Ecoponto; centralizados, a 50 mm da linha vermelha e separados por 100 mm | Marcações para o árbitro posicionar de uma a cinco plataformas por partida. A cor do piso indica o local, não o destino por si só: observar a plataforma colocada ali. |
| Quadrados cinza muito claro | Posições candidatas impressas, inclusive sobre ruas | Marcam possíveis posições de cubos. São cinza muito claros para não interferir na leitura de linha; não confundir com a cor cinza da lista oficial de reciclagem (que não é usada como cubo nesta prova). |
| Quadrados marrons no centro da cidade | Posições possíveis de cubos de obstáculo de **50 × 50 × 50 mm** | Obstáculos deliberados para sensores de distância. Não tocar, pegar, empurrar ou deslocar, nem incidentalmente durante tentativa de pegar outro cubo. Tratar a via como bloqueada e procurar rota alternativa. |

### Identificação impressa das posições (Figura 5 do regulamento)

- Pontos cinza **sobre as ruas transversais**: letras **A** e **B**, numeradas de **1 a 5**; letra **C**, de **1 a 3**.
- Pontos cinza **entre a área livre e o centro**: letras **D, E, F e G**, cada uma numerada de **1 a 3**.
- Obstáculos marrons no centro entre ruas: letras **X** e **Y**, cada uma numerada de **1 a 4**; posições centrais: **Z1** e **Z2**.
- A identificação de cada metade é espelhada. O desenho da arena oficial (Figuras 1, 2 e 5) é a referência espacial; não inferir coordenadas métricas ou sequência de rota apenas pelos nomes.

O mapa apresenta grades de ruas horizontais e verticais. As linhas pretas se cruzam; a pose inicial é aleatória e a configuração de cubos/plataformas pode mudar a cada partida. Codificar uma rota fixa sem localização e validação sensorial é insuficiente. Usar os IDs impressos como linguagem da equipe para mapear e validar cada posição quando o mapa real estiver disponível.

## 4. Objetos e destinos

### Cubos

- Plástico impresso em 3D, superfícies externas lisas; **50 × 50 × 50 mm**, **25 a 40 g**.
- Cores efetivamente usadas: **azul, vermelho, verde, amarelo, preto, branco e marrom**.
- Cada lado terá, à disposição do árbitro, cinco cubos de cada cor e seis brancos (**36 no total**); quantidade e distribuição da partida podem ser definidas pelo árbitro no começo ou durante a prova e podem ser simétricas.
- Códigos de reciclagem no contexto do desafio: azul = papel/papelão; vermelho = plástico; verde = vidro; amarelo = metal; preto = madeira; marrom = orgânico; branco = resíduo de saúde/identificação especial na tarefa. São categorias do desafio; a regra operacional específica para branco é não recolher.

### Plataformas

- Plástico, **160 × 50 × 50 mm**, peso de **400 a 500 g**; comporta até cinco cubos desde que permaneçam sobre ela.
- Há destinos para **azul, vermelho, verde, amarelo, preto e marrom**. Não há plataforma exclusiva branca.
- O árbitro coloca de **uma a cinco plataformas de cores distintas** nos retângulos brancos do Ecoponto imediatamente antes da partida. Posição e conjunto variam. Observar e mapear no início; não presumir quais destinos existem nem sua ordem.
- A plataforma é considerada deslocada para penalidade se mover mais de **10 mm** de sua posição de referência.

### Objetos que não devem ser recolhidos

1. **Cubo marrom colocado num quadrado marrom central:** obstáculo. Nunca manipular/deslocar, mesmo por acidente. Penalidade de obstáculo não identificado pode ser aplicada; árbitro recoloca-o na posição original.
2. **Cubo branco colocado num quadrado cinza:** se identificado corretamente e mantido onde estava, não é penalizado. Emitir sinal sonoro ou luminoso ao identificá-lo para que o árbitro possa reconhecê-lo como “cubo branco identificado”; vale **50 pontos uma única vez por cada cubo branco** durante toda a partida. Não mover.
3. **Cubo de cor para a qual não existe plataforma correspondente naquela partida:** o árbitro pode posicioná-lo na cidade. Identificar, deixar exatamente na posição e sinalizar como branco; a via deve ser considerada bloqueada e o robô deve buscar outro caminho. Recebe a mesma pontuação de identificação de cubo branco.

Não confundir “cubo marrom obstáculo em posição marrom” com “cubo marrom reciclável em ponto cinza”: o primeiro é sempre obstáculo; o segundo, se elegível e houver plataforma marrom, é carga de 100 pontos. É preciso considerar **posição, cor e destinos disponíveis**, não apenas classificar a cor.

## 5. Missão e máquina de estados recomendada

**Regra oficial:** no máximo **dois cubos por viagem/incursão à cidade**. Em uma incursão, o robô pode coletar um ou dois cubos; depois da coleta, deve obrigatoriamente ir à plataforma de destino correspondente e entregar todos os cubos transportados ou descartá-los antes de uma nova entrada na cidade. É vedado buscar um terceiro cubo ou coletar em nova incursão antes de concluir a entrega/descarte.

Uma implementação robusta deve manter estados explícitos e salvar a contagem/carga:

1. **AGUARDAR_INÍCIO:** aguardar o sinal autorizado de início. O método e a posição são definidos pelo árbitro; botão usado em testes não deve ser assumido como procedimento oficial.
2. **MAPEAR_ECOPONTO:** com o robô na área livre inicial, identificar pela cor as plataformas visíveis e registrar seus destinos/posições; no mínimo confirmar quais das seis cores existem. Não encostar nem deslocar.
3. **PLANEJAR_INCÚRSÃO:** criar/atualizar mapa local da cidade, escolher rota para cubo elegível, levando em conta limite, cubos/ruas bloqueados, obstáculo e tráfego do oponente.
4. **SEGUIR_ROTA:** seguir linha preta e cruzamentos com leitura contínua dos dois sensores de chão; acompanhar odometria/rumo se calibrados. Evitar colisão e fazer verificação de linha após cruzamentos.
5. **AVALIAR_ALVO:** usar distância para aproximar-se sem contato; classificar cor apenas quando o sensor de garra tiver distância, iluminação e ângulo calibrados. Combinar cor + posição + plataforma disponível. Se leitura não confiável, não pegar.
6. **SINALIZAR_E_DESVIAR (branco/não elegível):** deixar o cubo intacto e no local; sinalizar luz ou som, marcar posição como bloqueada para planejamento e recalcular. A pontuação oficial de branco identificado é única por objeto.
7. **COLETAR:** só alvo elegível, somente se carga atual permitir (máximo dois na incursão) e a coleta não arriscar obstáculo/cubo adjacente. Confirmar fisicamente/sensorialmente que a garra reteve o cubo antes de contar carga. Interromper se qualquer sensor indicar limite vermelho ou obstáculo próximo.
8. **RETORNAR_E_ENTREGAR:** retornar ao Ecoponto e navegar para a plataforma da cor correta. Soltar o cubo somente sobre a plataforma. “Entregue” significa permanecer estático sobre a plataforma correspondente; não precisa estar completamente contido. Um cubo em plataforma errada é perdido e retirado pelo árbitro.
9. **VERIFICAR_DESCARGA:** confirmar que cada cubo ficou parado sobre o destino correto e que cubos anteriormente colocados não caíram. Atualizar inventário/carga apenas após verificação. Não tocar a plataforma (margem >10 mm = infração).
10. **REPLANEJAR:** só após entregar todos os cubos transportados ou descartá-los, iniciar outra incursão. Voltar ao passo 3; evitar repetir alvos concluídos ou cubos brancos já pontuados.
11. **RECUPERAR_BLOQUEIO:** parar, recuar dentro da pista, reassociar-se à linha/mapa e recalcular. Não insistir empurrando obstáculo, oponente, cubo inelegível ou plataforma.
12. **PARAR_SEGURO:** ao fim de partida, falha de comunicação entre hubs, leitura crítica de limite, estado de trajetória incerto ou watchdog vencido, parar motores de tração; manter mecanismos em estado seguro.

### Prioridade de decisão a cada ciclo de controle

1. **Vermelho no chão / risco de sair da arena:** frear imediatamente e corrigir para dentro.
2. **Colisão iminente (objeto/oponente) ou caminho obstruído:** frear antes do contato; avaliar desvio seguro.
3. **Perda da linha preta ou pose/localização incerta:** parar/recuar com cautela e readquirir linha; não continuar uma rota cega.
4. **Regras de carga/destino:** nunca coletar acima de dois nem entrar para nova coleta com carga pendente.
5. **Classificação e pontuação:** somente coletar cubo elegível com cor e destino verificados.
6. **Eficiência:** entre caminhos seguros e legais, escolher o menor custo/tempo estimado.

## 6. Navegação e prevenção de colisão

- Seguir as ruas pretas **de forma consistente**; perda evidente de trajetória caracteriza robô perdido. Os sensores inferiores A e B leem HSV e permitem detectar linha/contraste, mas os limiares de classificação precisam ser calibrados na lona de competição.
- Qualquer leitura de vermelho por qualquer sensor de chão deve ter prioridade imediata. Não avançar no limite vermelho; recuar/virar para o interior. A penalidade oficial por ultrapassar a área permitida/sair da arena é **-5** e reposicionamento do robô na área livre inicial.
- Azul marca a fronteira da área livre/cidade. O robô pode acessar sua cidade e seu Ecoponto, mas não cruzar para a área livre da equipe oposta. Cruzar a linha azul do outro lado caracteriza robô perdido; regra de pontuação de invasão de área também prevê -5 e reposicionamento.
- Ultrassom frontal pode indicar algo à frente, mas não identifica cor, categoria, coordenada ou se o objeto é cubo branco, cubo marrom, cubo reciclável ou oponente. Confirmar com sensor de cor de perto antes de manipular. Limite de parada deve considerar largura do robô, balanço da garra e distância de frenagem.
- Encontro frontal com outro robô sobre a linha: ambos devem detectar, retornar e buscar rota alternativa. Quem insistir e empurrar o outro para fora da pista/via recebe **-10** e retorna ao ponto de partida; o robô deslocado é reposicionado pelo capitão.
- Encontro perpendicular em cruzamento: o robô que entrou por último é responsável por evitar colisão se os sensores permitiriam fazê-lo; infração: **-10** e retorno ao ponto de partida. Robô deslocado é reposicionado pelo capitão.
- Aproximação traseira: quem alcança o outro deve detectar e ajustar; colidir/empurrar gera **-10** e retorno ao ponto de partida. Robô atingido é reposicionado pelo capitão.
- O árbitro analisa e aplica penalidades de colisão; a responsabilidade de calibrar reação é da equipe. Situações omissas cabem à organização.
- O lado da equipe é espelhado, mas posição inicial aleatória e disposição dinâmica exigem percepção local; não assumir posição fixa no início.

## 7. Reconhecimento de cores: limites e protocolo

**Sensores listados no projeto**

| Hub/porta | Dispositivo no mapa atual | Uso possível | Limite conhecido |
|---|---|---|---|
| HubDriver A | Sensor de cor inferior esquerdo | HSV do piso, linha/zonas sob o lado esquerdo | Referências registradas são amostras, não faixas validadas. |
| HubDriver B | Sensor de cor inferior direito | HSV do piso, linha/zonas sob o lado direito | Idem; leituras podem divergir por iluminação, altura e posição. |
| HubClaw A | Sensor de cor junto à garra | HSV do cubo quando alinhado e perto | Ainda não há calibração de cubos; não usar amostras de piso como calibração de cubo. |
| HubClaw E | Ultrassom frontal | Distância aproximada ao objeto frontal | Não classifica cor nem semântica; ecos variam com geometria e orientação. |
| HubClaw F | “Side sensor” | Possível leitura lateral | Tipo/modelo e comportamento não registrados; não depender dele até confirmar. |
| Motores/encoders | Quatro motores de tração; motores de garra/elevador | Movimento e odometria/posição mecânica se calibrados | Direções, escala, precisão e referência do mecanismo ainda exigem validação física. |

**Amostras atuais de HSV do piso:** estão em `hub_driver/constants.py` e `docs/hardware_map.md` para azul, vermelho, verde, amarelo, preto, branco e marrom. São referências iniciais; não são bandas de decisão confiáveis. HSV do piso não é HSV de cubo.

Antes do evento, calibrar HSV dos sete cubos reais com o sensor HubClaw A na distância/ângulo reais; calibrar piso de cada sensor HubDriver nas condições de luz reais; incluir várias leituras, dispersão, limiar de rejeição e categoria **DESCONHECIDO**. Se a distância ao cubo for inadequada, sensor saturar, ou a classificação ficar entre classes, não pegar. Validar novamente ao trocar a lona, iluminação, altura de montagem ou sensor.

Um mapeamento por cor só classifica as seis cores que têm destino quando aquela plataforma existe. Antes de coletar: `classe confiável?` AND `não é branco?` AND `não está em ponto de obstáculo?` AND `há plataforma da mesma cor?` AND `capacidade da incursão < 2?`. Se qualquer resposta for negativa ou desconhecida, preservar o cubo e evitar a via.

## 8. Limites mecânicos e de atuação

- Um robô por equipe. Hardware livre, incluindo controladores, sensores, atuadores e kits educacionais; exceção expressa: **câmeras, LiDAR ou similares e processamento de imagens são proibidos**.
- Largura e comprimento máximos: **300 × 300 mm** em todos os momentos, inclusive garra/braço/extensor totalmente aberto e operação. Altura não tem limite especificado.
- Garra/elevador não podem exceder o envelope. Levantamento físico da dimensão totalmente estendida antes do evento.
- Valores anotados no projeto (referenciais, não automaticamente seguros): garra aberta 389°, fechada -60°; elevador baixo 197° (garra ~5 mm do chão), alto -1262° (garra ~75 mm). Manter referência de ângulo; conferir se sobrevive ao início e aos ciclos de energia. Não atingir batente mecânico em alta velocidade nem apertar cubo até deformá-lo.
- Tráfego por BLE entre os dois hubs embarcados é comunicação interna do robô, não controle externo. Definir protocolo com heartbeat, watchdog e mensagem de parada; perda de comunicação deve parar tração. Comunicação externa ou comando humano não pode decidir/navegar o robô durante a partida, salvo autorização expressa do árbitro.

## 9. Pontuação (regulamento v1.0)

| Evento | Pontos / ação oficial |
|---|---|
| Cada cubo vermelho, marrom elegível, azul, verde, preto ou amarelo entregue sobre sua plataforma correspondente | **+100** |
| Cubo branco corretamente identificado e sinalizado, sem mover do lugar | **+50 por cubo branco**, uma única vez por cubo durante a partida |
| Cubo de cor sem plataforma no jogo, identificado, deixado no lugar e sinalizado | Mesma pontuação do cubo branco (**+50**) e via bloqueada |
| Cubo branco retirado de sua posição inicial por mais de 50% da área, sem identificação | **-15** |
| Cubo perdido ou alvo deslocado sem sucesso, conforme seção de observações | **-10**; árbitro repõe no lugar original nos casos descritos |
| Plataforma movida mais de 10 mm no Ecoponto | **-20** |
| Obstáculo não identificado / deslocamento de obstáculo marrom central | **-15** |
| Robô ultrapassa sua área permitida ou sai da arena | **-5**, capitão reposiciona na área livre inicial |
| Cada reinício após equipe tocar/recolocar/reiniciar o robô ou remontar peça | **-15** |
| Robô inativo | **-10**; inatividade intencional por mais de 1 minuto para evitar pontuação negativa é desistência |
| Cada reposicionamento de cubo nos quadrados cinza durante a partida | **-5** |
| Derruba cubo já pontuado ao tentar usar a mesma plataforma | Subtrai **45 pontos da pontuação anterior**; cubo é reposicionado na posição inicial e pode ser coletado por qualquer equipe |
| Cubo colocado em plataforma errada | Considerado perdido; árbitro retira da plataforma e repõe no local inicial |

As pontuações negativas não levam o total final abaixo de zero. O regulamento também define regras para cubos deixados na área livre, ajustes antes da alocação (até 30 s e cubo integralmente dentro da área livre) e reposicionamento pelo árbitro; casos concretos devem ser levados ao árbitro, pois o texto usa mais de uma formulação de “cubo perdido”.

**Critério de entrega:** cubo deve permanecer estático sobre plataforma correspondente; pode ficar parcialmente para fora, desde que sobre ela. Na prática, mirar no centro reduz queda. Verificar que o robô não derrubou cubos antigos.

## 10. Relógio, fim de partida, desempate e reinícios

- Duração máxima normal: **12 minutos**.
- A partida encerra automaticamente se todos os cubos forem posicionados corretamente nos destinos. Ao time-out, vence a maior pontuação.
- Overtime: se o árbitro identificar empate próximo ao fim e totais positivos, pode dar até **3 minutos**; nesse período vence a primeira equipe que fizer uma tarefa de pontuação positiva. Se ninguém pontuar positivamente até 15 min, usam-se os critérios de desempate 0×0.
- Desempate 0×0, em ordem: maior pontuação positiva; se igual, menos pontuações negativas; se nenhuma tarefa somou pontos positivos, empate na classificação; em mata-mata, árbitro avalia junto aos capitães quem chegou mais perto do objetivo.
- Give-up: se uma equipe desistir, o adversário vence se o robô continuar na pista demonstrando tentativa ativa por pelo menos dois minutos; sem condições mínimas, empate.
- Toque humano, reposicionamento, reinício de programa ou remontagem de peça pelo time é **reinício**, penalizado em -15. O árbitro/capitão pode fazer o reposicionamento indicado pelas regras após infração; não confundir isso com correção autônoma normal.
- Robô parado ou movendo sem relação com os desafios pode ser considerado inativo (-10). Retirar/deixar inativo intencionalmente por mais de um minuto para evitar pontuação negativa é desistência.

## 11. O que os sensores atuais permitem afirmar — e o que não permitem

O inventário em código dá dois sensores de cor no piso, um sensor de cor na garra, um ultrassom frontal e um sensor lateral de tipo desconhecido. Isso permite construir detecção de linhas/cores, aproximação por distância e classificação de objeto próximo após calibração. **Não demonstra** localização global da pose inicial aleatória, detecção omnidirecional de oponente, reconhecimento confiável de cor à distância, confirmação de cubo agarrado, identificação automática de plataformas sem varredura, nem evitar todos os obstáculos. Não prometer essas capacidades até desenvolver e comprovar sensores, geometria e software.

O sonar frontal deve ser usado como zona de parada; o sensor de garra, como classificador de perto; sensores inferiores, como guarda contínua de limite e guia de linha. O sensor lateral só entra no algoritmo depois de identificar modelo/alcance/campo de visão. Motores podem apoiar odometria, mas escorregamento, giro e erros acumulados precisam ser corrigidos com as linhas e leituras reais.

## 12. Estado atual do software e lacunas prioritárias

Arquivos base: `hub_driver/`, `hub_claw/`, `docs/hardware_map.md`, `docs/arena_readiness.md`.

- `hub_driver/autonomous_driver.py` e `hub_claw/autonomous_pickup.py` são uma prova de conceito de aproximação frontal de um objeto, com mensagem BLE `FWD`/`STOP`; não fazem mapa/rota pela arena, classificação de cores, seleção de destino, navegação por linha ou entrega.
- A rotina de garra aproxima-se de **qualquer objeto** no alcance e pode fechar/levantar sem confirmar cor ou elegibilidade. Não usá-la como programa de partida.
- Ainda faltam máquina de estados completa, protocolo bidirecional de carga/destino/falha, mapa de rotas, seguir linhas, recuperação de linha, detecção de oponente, evitar vias bloqueadas, classificador com rejeição, confirmação de pega/entrega e sinal oficial de cubo branco.
- A documentação marca pendente: tipo do sensor HubClaw F, direção/orientação dos motores e mecanum, distância por grau/precisão de giro, HSV real, referência dos atuadores após reinício, ângulo de preensão, mapa de plataformas, protocolo BLE, envelope estendido e ensaios completos.
- A versão atual dos arquivos não deve ser chamada de autônoma/certificada. Um upload bem-sucedido não prova prontidão física.

## 13. Plano mínimo de validação antes de uma partida

1. Verificar no hardware real porta/tipo/orientação de cada sensor e motor, inclusive confirmar HubClaw F.
2. Medir robô inteiro com todos os mecanismos completamente estendidos: máximo 300 × 300 mm.
3. Calibrar sensor de cor do chão para linhas preta, vermelha, azul, verde, amarela e zonas em ambos os lados e em luz real; validar parada imediata no vermelho.
4. Calibrar separadamente o sensor da garra nos sete cubos reais e classes desconhecidas; medir taxa de confusão e rejeitar leituras incertas.
5. Testar ultrassom em cubos, paredes/plataformas e robô oponente em ângulos reais; definir distância segura de frenagem para velocidade e carga máximas.
6. Testar sentido das quatro rodas suspensas e no chão, movimentos longitudinal/lateral/rotação; medir odometria e erro em cada cruzamento.
7. Confirmar que ângulos de garra/elevador são válidos após inicialização e ciclos de energia; executar lento, sem batente e com cubo real.
8. Validar recolha e entrega de um cubo de cada cor elegível; observar estabilidade na plataforma e se plataforma move mais de 10 mm.
9. Testar casos negativos: cubo branco, cor sem plataforma, obstáculo marrom na posição central, objeto desconhecido, plataforma ausente, leitura ambígua, linha vermelha, perda de linha, oponente em cada geometria e timeout BLE.
10. Confirmar sinal sonoro/luminoso perceptível para o árbitro ao identificar cubo não coletável e garantir que cada cubo branco pontue no máximo uma vez.
11. Repetir partida completa abaixo de 12 minutos, com início aleatório, configuração variável e duas equipes/obstáculos; conferir inventário e limite de dois cubos por incursão.

## 14. Regras de trabalho para agentes e chats futuros

Ao trabalhar neste repositório:

1. Ler este guia e `docs/hardware_map.md` antes de alterar navegação, percepção ou manipulação.
2. Tratar o PDF oficial e decisões recentes do árbitro/organização como autoridade; preservar distinção entre **regra**, **estado verificado**, **inferência** e **pendência**.
3. Nunca inventar capacidade de sensor, coordenadas, disposição de plataforma ou regra de pontuação. Se desconhecido, marcar como desconhecido e escolher comportamento conservador.
4. Não mudar números de porta, sentido, calibrações, limites físicos ou lógica de segurança sem evidência/teste no hardware real e atualização deste guia/mapa.
5. Não iniciar movimento autônomo de competição em teste de bancada; testes de motor/garra requerem supervisão e espaço seguro.
6. Toda estratégia/alteração deve preservar: autonomia embarcada; sem câmera/LiDAR/imagem; dimensões; dois cubos por incursão; entrega antes da próxima; branco/não elegível intocado; obstáculo marrom intocado; parada imediata no vermelho; prevenção de colisão e falha segura.
7. Ao descobrir uma mudança, atualizar este documento e `docs/arena_readiness.md` para que a memória compartilhada permaneça atualizada.

## 15. Referências internas e oficiais

- Regulamento fornecido: *Regras_Challenge_2026_Portugues-V1.0.pdf* (seções 2–9; figuras 1–5). Arquivo de origem informado pela equipe: `C:\Users\User\Downloads\Regras_Challenge_2026_Portugues-V1.0.pdf`.
- `docs/hardware_map.md`: ligações, ângulos e referências atuais.
- `docs/arena_readiness.md`: checklist técnico e pendências de validação.
- `hub_driver/constants.py`, `hub_driver/ground_sensors.py`: portas e amostras do chão.
- `hub_claw/constants.py`, `hub_claw/sensors.py`, `hub_claw/autonomous_pickup.py`: portas e prova de conceito atual.

