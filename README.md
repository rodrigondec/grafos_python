<h1>Grafos</h1>
<p>Implementação da representação dos vários tipos de grafos em Python</p>
<h2>Nós</h2>
<h3>Tipos</h3>
<ul>
	<li>
		<label><b>Nó simples</b> | "<b>No</b>"</label>
		<p>
			A classe implementada para o nó simple está implementada no arquivo "<b>No.py</b>". <br>
			Ela possui o atributo <i>identificador</i> que pode ser tanto um inteiro quanto uma string, e um método para retornar o nó como string. <br />
			Por exmplo se possuirmos um nó no qual <i>identificador</i> = <b>1</b>, sua string ficará será "[1]".
		</p>
		<p></p>
	</li>
	<li>
		<label><b>Nó valorado</b> | "<b>NoValorado</b>"</label>
		<p>
			A classe implementada para o nó valorado está implementada no arquivo "<b>No.py</b>". <br>
			Ela é uma extensão da classe "<b>No</b>" citada acima com o acréscimo do atributo <i>valor</i>. <br>
			O stringfy herdado da classe foi adaptada para acrescentar o atributo <i>valor</i>. <br />
			Por exmplo se possuirmos um nó no qual <i>identificador</i> = <b>1</b> e <i>valor</i> = <b>15</b>, sua string ficará será "[1] {15}".
		</p>
	</li>
</ul>
<h2>Arestas</h2>
<h3>Tipos</h3>
<ul>
	<li>
		<label><b>Aresta simples</b> | "<b>Aresta</b>"</label>
		<p>
			A classe implementada para a aresta simples está implementada no arquivo "<b>Aresta.py</b>". <br>
			Ela possui dois atributos <i>identificador1</i> e <i>identificador2</i> que são referentes aos identificadores dos dois nós conexos, e um método para retornar a aresta como string. <br />
			Por exmplo se possuirmos uma aresta na qual liga o nó <i>identificador</i> = <b>1</b> com o nó <i>identificador</i> = <b>2</b>, sua string ficará será "[1, 2]".
		</p>
		<p></p>
	</li>
	<li>
		<label><b>Aresta valorada</b> | "<b>ArestaValorada</b>"</label>
		<p>
			A classe implementada para a aresta valorada está implementada no arquivo "<b>Aresta.py</b>". <br>
			Ela é uma extensão da classe "<b>Aresta</b>" citada acima com o acréscimo do atributo <i>valor</i>. <br> 
			O stringfy herdado da classe foi adaptada para acrescentar o atributo <i>valor</i>.
			Por exmplo se possuirmos uma aresta na qual liga o nó <i>identificador</i> = <b>1</b> com o nó <i>identificador</i> = <b>2</b> com um <i>valor</i> = <b>15</b>, sua string ficará será "[1, 2] {15}".
		</p>
	</li>
</ul>
<h2>Grafos</h2>
<h3>Tipos</h3>
<ul>
	<li>
		<label><b>Grafo simples</b> | "<b>Grafo</b>"</label>
		<p>
			A classe implementada para o grafo simples está implementada no arquivo "<b>grafo.py</b>". <br>
			Ela possui dois atributos <i>nós</i> e <i>arestas</i> que são listas para armazenar os respectivos objetos do grafo. <br>
			Essa classe também possui os seguintes métodos:
			<ul>
				<li><i>existsNo(identificador)</i>: método que retorna um boolean true se o nó de <i>identificador</i> existir no grafo.</li>
				<li><i>existsAresta(identificador1, identificador2)</i>: método que retorna um boolean true se a aresta de <i>identificador1</i> e <i>identificador2</i> existir no grafo.</li>
				<li><i>insertNo(no)</i>: método que insere o <i>nó</i> passado como parâmetro no grafo.</li>
				<li><i>insertAresta(aresta): método que insere a <i>aresta</i> passada como parâmetro no grafo.</i></li>
				<li><i>printNos()</i>: método que imprime todos os nós do grafo.</li>
				<li><i>printArestas()</i>: método que imprime todas as arestas do grafo.</li>
				<li><i>str()</i>: método que imprime todo o grafo. seguindo o modelo "( <b>nó 1</b>, <b>nó 2</b>, <b>nó n</b>; <b>aresta 1</b>, <b>aresta 2</b>, <b>aresta n</b> )"</li>
			</ul>
		</p>
		<p></p>
	</li>
	<li>
		<label><b>Grafo simples com nó valorado</b> | "<b>Grafo_ArestaValorada</b>"</label>
		<p>
			A classe implementada para o grafo simples com nó valorado está implementada no arquivo "<b>grafo.py</b>". <br>
			Ela é uma extensão da classe "<b>Grafo</b>" citada acima com o acréscimo do atributo <i>valor</i>. <br> 
			O stringfy herdado da classe foi adaptada para acrescentar o atributo <i>valor</i>.
			Por exmplo se possuirmos uma aresta na qual liga o nó <i>identificador</i> = <b>1</b> com o nó <i>identificador</i> = <b>2</b> com um <i>valor</i> = <b>15</b>, sua string ficará será "[1, 2] {15}".
		</p>
	</li>
</ul>