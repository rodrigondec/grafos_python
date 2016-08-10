<h1>Grafos</h1>
<p>Implementação da representação dos vários tipos de grafos em Python</p>
<h2>Nós</h2>
<h3>Tipos</h3>
<ul>
	<li>
		<label><b>Nó simples</b></label>
		<p>
			A classe implementada para o nó simple está implementada no arquivo "<b>No.py</b>". <br>
			Ela possui o atributo <i>identificador</i> que pode ser tanto um inteiro quanto uma string, e um método para retornar o nó como string. <br />
			Por exmplo se possuirmos um nó no qual <i>identificador</i> = <b>1</b>, sua string ficará será "[1]".
		</p>
		<p></p>
	</li>
	<li>
		<label><b>Nó valorado</b></label>
		<p>
			A classe implementada para o nó valorado está implementada no arquivo "<b>No.py</b>". <br>
			Ela é uma extensão da classe "<b>No</b>" citada a cima com o acréscimo do atributo <i>valor</i>. <br>
			O stringfy herdado da classe foi adaptada para acrescentar o atributo <i>valor</i>. <br />
			Por exmplo se possuirmos um nó no qual <i>identificador</i> = <b>1</b> e <i>valor</i> = <b>15</b>, sua string ficará será "[1] {15}".
		</p>
	</li>
</ul>
<h2>Arestas</h2>
<h3>Tipos</h3>
<ul>
	<li>
		<label><b>Aresta simples</b></label>
		<p>
			A classe implementada para a aresta simples está implementada no arquivo "<b>Aresta.py</b>". <br>
			Ela possui dois atributos <i>identificador1</i>, <i>identificador2</i> (que serão referentes aos identificadores dos dois conexos) e um método para retornar a aresta como string. <br />
			Por exmplo se possuirmos uma aresta na qual liga o nó <i>identificador</i> = <b>1</b> com o nó <i>identificador</i> = <b>2</b>, sua string ficará será "[1, 2]".
		</p>
		<p></p>
	</li>
	<li>
		<label><b>Aresta valorada</b></label>
		<p>
			A classe implementada para a aresta valorada está implementada no arquivo "<b>Aresta.py</b>". <br>
			Ela é uma extensão da classe "<b>Aresta</b>" citada a cima com o acréscimo do atributo <i>valor</i>. <br> 
			O stringfy herdado da classe foi adaptada para acrescentar o atributo <i>valor</i>.
			Por exmplo se possuirmos uma aresta na qual liga o nó <i>identificador</i> = <b>1</b> com o nó <i>identificador</i> = <b>2</b> com um <i>valor</i> = <b>15</b>, sua string ficará será "[1, 2] {15}".
		</p>
	</li>
</ul>
<h2>Grafos</h2>
<h3>Tipos</h3>
<ul>
	<li>
		<label><b>Grafo simples</b></label>
		<p>
			A classe implementada para o grafo simples está implementada no arquivo "<b>grafo.py</b>". <br>
			Ela possui dois atributos <i>nós</i>, <i>arestas</i> que são listas para armazenas os respectivos objetos do grafo. <br>
			Essa classe também possui os seguintes métodos:
			<ul>
				<li><i>existsNo(identificador)</i></li>
				<li><i>existsAresta(identificador1, identificador2)</i></li>
				<li><i>insertNo(no)</i></li>
				<li><i>insertAresta(aresta)</i></li>
				<li><i>printNos()</i></li>
				<li><i>printArestas()</i></li>
				<li><i>str()</i></li>
			</ul>
			Por exmplo se possuirmos uma aresta na qual liga o nó <i>identificador</i> = <b>1</b> com o nó <i>identificador</i> = <b>2</b>, sua string ficará será "[1, 2]".
		</p>
		<p></p>
	</li>
	<li>
		<label><b>Aresta valorada</b></label>
		<p>
			A classe implementada para a aresta valorada está implementada no arquivo "<b>Aresta.py</b>". <br>
			Ela é uma extensão da classe "<b>Aresta</b>" citada a cima com o acréscimo do atributo <i>valor</i>. <br> 
			O stringfy herdado da classe foi adaptada para acrescentar o atributo <i>valor</i>.
			Por exmplo se possuirmos uma aresta na qual liga o nó <i>identificador</i> = <b>1</b> com o nó <i>identificador</i> = <b>2</b> com um <i>valor</i> = <b>15</b>, sua string ficará será "[1, 2] {15}".
		</p>
	</li>
</ul>