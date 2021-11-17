from django.db import models

TESTE_HIV = (
    ('TR', 'TR'),
    ('PCRE', 'PCRE'),
)


class Location(models.Model):
    location_id = models.CharField(max_length=500, primary_key=True)
    codigo = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    state_province = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    parent_location = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Paciente(models.Model):
    patient_id = models.CharField(max_length=500, primary_key=True)
    nid = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=20)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=100, blank=True, null=True)
    profissao = models.CharField(max_length=100, blank=True, null=True)
    livro = models.CharField(max_length=15, blank=True, null=True)
    pagina = models.CharField(max_length=4, blank=True, null=True)
    linha = models.CharField(max_length=4, blank=True, null=True)
    nome_confidente = models.CharField(max_length=255, blank=True, null=True)
    confidente_parentesco = models.CharField(
        max_length=255, blank=True, null=True)
    telefone1_confidente = models.CharField(
        max_length=255, blank=True, null=True)
    telefone2_confidente = models.CharField(
        max_length=255, blank=True, null=True)
    endereco_confidente = models.CharField(
        max_length=500, null=True, blank=True)
    distrito = models.CharField(max_length=100, null=True, blank=True)
    posto_administrativo = models.CharField(
        max_length=100, null=True, blank=True)
    localidade = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    ponto_referencia = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome


class TesteHivPos(models.Model):
    tipo_teste = models.CharField(max_length=10, choices=TESTE_HIV)
    data_teste = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.tipo_teste


class Inscricao(models.Model):
    paciente = models.OneToOneField(
        Paciente, on_delete=models.CASCADE, primary_key=True)
    data_abertura = models.DateTimeField(null=True, blank=True)
    data_diagnostico = models.DateTimeField(null=True, blank=True)
    inscrito_programa = models.CharField(max_length=10, blank=True, null=True)
    data_inscricao_programa = models.DateTimeField(null=True, blank=True)
    data_inicio_tarv = models.DateTimeField(null=True, blank=True)
    morreu = models.BooleanField(default=False, null=True, blank=True)
    referencia = models.CharField(max_length=255, null=True, blank=True)
    data_morte = models.DateTimeField(null=True, blank=True)
    hepatite = models.BooleanField(default=False, null=True, blank=True)
    data_hepatite = models.DateTimeField(null=True, blank=True)
    diabetes = models.BooleanField(default=False, null=True, blank=True)
    data_diabetes = models.DateTimeField(null=True, blank=True)
    tb = models.BooleanField(default=False, null=True, blank=True)
    data_tb = models.DateTimeField(null=True, blank=True)
    hta = models.BooleanField(default=False, null=True, blank=True)
    data_hta = models.DateTimeField(auto_now=False, null=True, blank=True)
    criptococose = models.BooleanField(default=False, null=True, blank=True)
    data_criptococose = models.DateTimeField(
        null=True, blank=True)
    s_kapose = models.BooleanField(default=False, null=True, blank=True)
    data_kapose = models.DateTimeField(null=True, blank=True)
    via_positivo = models.BooleanField(default=False, null=True, blank=True)
    data_via = models.DateTimeField(null=True, blank=True)
    outra = models.CharField(max_length=255, null=True, blank=True)
    data_outra = models.DateTimeField(null=True, blank=True)
    ultimo_cd4 = models.IntegerField(null=True, blank=True)
    data_cd4 = models.DateTimeField(null=True, blank=True)
    ultima_cv = models.IntegerField(null=True, blank=True)
    data_cv = models.DateTimeField(auto_now=False, null=True)
    ultima_ctz_data_inicio = models.DateTimeField(
        null=True, blank=True)
    ultima_ctz_data_fim = models.DateTimeField(blank=True, null=True)
    gravidez = models.BooleanField(default=False, null=True, blank=True)
    lactante = models.BooleanField(default=False, null=True, blank=True)
    estadio_oms = models.CharField(max_length=10, null=True, blank=True)
    data_estadio_oms = models.DateTimeField(null=True, blank=True)
    transferido_em = models.CharField(max_length=255, null=True, blank=True)
    data_transferencia = models.DateTimeField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Inscricoes'

    def __str__(self):
        return self.paciente.nome


class DiagnosticoITS(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


class ConsultaClinica(models.Model):
    data_consulta = models.DateTimeField(null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_proxima_consulta = models.DateTimeField(null=True, blank=True)
    populacao_chave = models.CharField(max_length=100, blank=True, null=True)
    populacao_vulneravel = models.CharField(
        max_length=100, blank=True, null=True)
    gravidez = models.CharField(max_length=100, null=True, blank=True)
    lactante = models.CharField(max_length=100, null=True, blank=True)
    data_ultima_menstruacao = models.DateTimeField(
        null=True, blank=True)
    tensao_arterial = models.CharField(max_length=100, blank=True, null=True)
    estadio_OMS = models.CharField(max_length=100, blank=True, null=True)
    peso = models.DecimalField(
        decimal_places=2, max_digits=2, null=True, blank=True)
    crianca_edemas = models.CharField(max_length=100, blank=True, null=True)
    altura = models.DecimalField(
        decimal_places=2, max_digits=2, null=True, blank=True)
    imc = models.DecimalField(
        decimal_places=2, max_digits=2, null=True, blank=True)
    tem_sintomas_tb = models.CharField(max_length=10, blank=True, null=True)
    diagnostico_tb_activo = models.CharField(
        max_length=10, blank=True, null=True)
    profilaxia_inh = models.CharField(max_length=10, blank=True, null=True)
    efeitos_secundarios_inh = models.CharField(
        max_length=10, blank=True, null=True)
    profilaxia_ctz = models.CharField(max_length=10, blank=True, null=True)
    efeitos_secundarios_ctz = models.CharField(
        max_length=10, blank=True, null=True)
    tratamento_tb = models.CharField(max_length=10, blank=True, null=True)
    data_tb = models.DateTimeField(null=True, blank=True)
    sintomas_tb = models.CharField(max_length=50, blank=True, null=True)
    tem_sintomas_its = models.CharField(max_length=50, blank=True, null=True)
    infecoes_oportunistas = models.CharField(
        max_length=155, blank=True, null=True)
    referencia_sector = models.CharField(max_length=255, blank=True, null=True)
    elegivel_grupo_apoio = models.CharField(
        max_length=255, blank=True, null=True)
    criancas_reveladas = models.CharField(
        max_length=255, blank=True, null=True)
    pais_cuidadores = models.CharField(max_length=255, blank=True, null=True)
    adolescentes_reveladas = models.CharField(
        max_length=255, blank=True, null=True)
    mae_para_mae = models.CharField(max_length=255, blank=True, null=True)
    elegivel_mdc = models.CharField(max_length=255, blank=True, null=True)
    gaac = models.CharField(max_length=255, blank=True, null=True)
    abordagem_familiar = models.CharField(
        max_length=255, blank=True, null=True)
    clubes_adesao = models.CharField(max_length=255, blank=True, null=True)
    paragem_unica = models.CharField(max_length=255, blank=True, null=True)
    fluxo_rapido = models.CharField(max_length=255, blank=True, null=True)
    dispensa_trimestral = models.CharField(
        max_length=255, blank=True, null=True)
    dispensa_semestral = models.CharField(
        max_length=255, blank=True, null=True)
    dispensa_comunitaria = models.CharField(
        max_length=255, blank=True, null=True)
    farmacia_privada = models.CharField(max_length=255, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Consulta Clinica'
        verbose_name_plural = 'Consultas Clinicas'

    def __str__(self):
        return self.paciente.nome


class ConsultaApss(models.Model):
    populacao_chave = models.CharField(max_length=100, blank=True, null=True)
    livro_apps = models.IntegerField()
    pagina_livro = models.IntegerField()
    linha_livro = models.IntegerField()
    consulta_actual = models.DateTimeField(auto_now=False)
    proxima_consulta = models.DateTimeField(auto_now=False)
    estado_revelacao_cr_adol = models.CharField(
        max_length=100, blank=True, null=True)
    educ_sobre_hiv = models.CharField(max_length=100, blank=True, null=True)
    recusa_resultado_pos = models.BooleanField(
        default=False, null=True, blank=True)
    sente_doent_demais = models.BooleanField(
        default=False, null=True, blank=True)
    nao_acredita_tarv = models.BooleanField(
        default=False, null=True, blank=True)
    muitos_comprimidos = models.BooleanField(
        default=False, null=True, blank=True)
    falta_alimentacao = models.BooleanField(
        default=False, null=True, blank=True)
    falta_apoio_familiar = models.BooleanField(
        default=False, null=True, blank=True)
    ansiedade = models.BooleanField(default=False, null=True, blank=True)
    difcdad_revelar_parceiro = models.BooleanField(
        default=False, null=True, blank=True)
    toxicidade = models.BooleanField(default=False, null=True, blank=True)
    perdeu_comprimidos = models.BooleanField(
        default=False, null=True, blank=True)
    estigma_ou_descriminacao = models.BooleanField(
        default=False, null=True, blank=True)
    problemas_transp = models.BooleanField(
        default=False, null=True, blank=True)
    vbg = models.BooleanField(default=False, null=True, blank=True)
    uso_alcool_drogas = models.BooleanField(
        default=False, null=True, blank=True)
    outro = models.CharField(max_length=100, null=True, blank=True)
    sexo_seguro = models.CharField(max_length=100, null=True, blank=True)
    revelacao_seroestado_parceiro = models.CharField(
        max_length=100, null=True, blank=True)
    importancia_adesao_tarv = models.CharField(
        max_length=100, null=True, blank=True)
    inf_transmissao_sexual = models.CharField(
        max_length=100, null=True, blank=True)
    pf_gs_ptv = models.CharField(max_length=100, null=True, blank=True)
    necess_apoio_comunitario = models.CharField(
        max_length=100, null=True, blank=True)
    oferta_lubrificantes = models.CharField(
        max_length=100, null=True, blank=True)
    informou_seroestado = models.CharField(
        max_length=100, null=True, blank=True)
    parentesco = models.CharField(max_length=100, null=True, blank=True)
    quem_administra_arv = models.CharField(
        max_length=100, null=True, blank=True)
    parentesco_administra = models.CharField(
        max_length=100, null=True, blank=True)
    horario_esq_dose_viagem = models.CharField(
        max_length=100, null=True, blank=True)
    efeitos_secundarios = models.CharField(
        max_length=100, null=True, blank=True)
    adesao_tarv = models.CharField(max_length=100, null=True, blank=True)
    motivo_consulta = models.CharField(max_length=100, null=True, blank=True)
    cr_revelada = models.CharField(max_length=100, null=True, blank=True)
    adolescente_revelado = models.CharField(
        max_length=100, null=True, blank=True)
    pais_cuidadores = models.CharField(max_length=100, null=True, blank=True)
    mae_para_mae = models.CharField(max_length=100, null=True, blank=True)
    gaac = models.CharField(max_length=100, null=True, blank=True)
    fluxo_rapido = models.CharField(max_length=100, null=True, blank=True)
    dispensa_trimestral = models.CharField(
        max_length=100, null=True, blank=True)
    dispensa_comunitaria = models.CharField(
        max_length=100, null=True, blank=True)
    dispensa_semestral = models.CharField(
        max_length=100, null=True, blank=True)
    concorda_ser_contactado = models.CharField(
        max_length=100, null=True, blank=True)
    data_consentimento = models.DateTimeField(
        auto_now=False, null=True, blank=True)
    tipo_contacto = models.CharField(max_length=100, null=True, blank=True)
    confidente_concorda_contacto = models.CharField(
        max_length=100, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Consulta Apss'
        verbose_name_plural = 'Consultas Apss'

    def __str__(self):
        return self.paciente.nome


class VisitaDomiciliaria(models.Model):
    livro_chamadas = models.IntegerField(null=True, blank=True)
    pagina_livro = models.IntegerField(null=True, blank=True)
    linha_livro = models.IntegerField(null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nome_casa = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    avenida_ou_rua = models.CharField(max_length=255, null=True, blank=True)
    aldeia_comunidade = models.CharField(max_length=255, null=True, blank=True)
    quarteirao = models.CharField(max_length=255, null=True, blank=True)
    numero_casa = models.CharField(max_length=255, null=True, blank=True)
    contacto_paciente = models.CharField(max_length=255, null=True, blank=True)
    ponto_referencia = models.CharField(max_length=255, null=True, blank=True)
    paciente_autorizou = models.CharField(
        max_length=255, null=True, blank=True)
    nome_confidente = models.CharField(max_length=255, null=True, blank=True)
    crianca_exposta = models.CharField(max_length=255, null=True, blank=True)
    bk = models.CharField(max_length=255, null=True, blank=True)
    tb_sem_tratamento = models.CharField(max_length=255, null=True, blank=True)
    sem_cv = models.CharField(max_length=255, null=True, blank=True)
    falencia_terapeutica = models.CharField(
        max_length=255, null=True, blank=True)
    elegivel_tarv = models.CharField(max_length=255, null=True, blank=True)
    faltoso_farmacia = models.CharField(max_length=255, null=True, blank=True)
    faltoso_consultas = models.CharField(max_length=255, null=True, blank=True)
    cv_elevada = models.CharField(max_length=255, null=True, blank=True)
    seguimento_preventivo = models.CharField(
        max_length=255, null=True, blank=True)
    outro = models.CharField(max_length=255, null=True, blank=True)
    servico_refere = models.CharField(max_length=255, null=True)
    voluntario = models.CharField(max_length=255, null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.paciente.nome


class RelatorioVisita(models.Model):
    tipo_visita = models.CharField(max_length=100)
    data_visita = models.DateTimeField(auto_now=False)
    motivo_falta = models.CharField(max_length=100, null=True, blank=True)
    relatorio_visita = models.CharField(max_length=100, null=True, blank=True)
    paciente_encaminhado_para = models.CharField(
        max_length=100, null=True, blank=True)
    data_para_retorno = models.DateTimeField(
        auto_now=False, null=True, blank=True)
    motivo_nao_encontrado = models.CharField(
        max_length=100, null=True, blank=True)
    info_dada_por = models.CharField(max_length=100, null=True, blank=True)
    contacto_informante = models.CharField(
        max_length=100, null=True, blank=True)
    data_devolucao_cartao = models.CharField(
        max_length=100, null=True, blank=True)
    pessoa_efectuou_visita = models.CharField(max_length=100)
    visita_domiciliaria = models.ForeignKey(
        VisitaDomiciliaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_visita


class ExameClinico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now=False)
    data_colheita = models.DateTimeField(auto_now=False)
    data_resultado = models.DateTimeField(auto_now=False)
    globulos_brancos = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    globulos_vermelhos = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    hemoglobina = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    hematorcito = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    vol_corpuscular_med = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    conc_media_hemoglob_corp = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    plaquetas = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    larg_distr_gv = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    velc_sedime_gv = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    vol_medio_plaquetas = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    tipagem_sanguinea = models.CharField(max_length=255, null=True, blank=True)
    linfocitos_perc = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    linfocitos_abs = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    neutrofilos_perc = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    neutrofilos_abs = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    eosinofilo_perc = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    eosinofilo_abs = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    basofio_perc = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    basofio_abs = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    monocito_perc = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    monocito_abs = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    teste_vdr = models.CharField(max_length=50, blank=True, null=True)
    rpr = models.CharField(max_length=50, blank=True, null=True)
    cd4_abs = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    cd4_perc = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    carga_viral = models.IntegerField()
    carga_viral_qualitativo = models.CharField(
        max_length=100, blank=True, null=True)
    geneexpert = models.CharField(max_length=50, blank=True, null=True)
    xpert_mtb = models.CharField(max_length=50, blank=True, null=True)
    nivel_mtb_detetado = models.CharField(max_length=50, blank=True, null=True)
    resistencia_rifampin = models.CharField(
        max_length=50, blank=True, null=True)
    cultura = models.CharField(max_length=50, blank=True, null=True)
    tb_lam = models.CharField(max_length=50, blank=True, null=True)
    baciloscopial = models.CharField(max_length=50, blank=True, null=True)
    nivel_positividade = models.CharField(max_length=50, blank=True)
    albumina = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    asparato_aminotransferiase = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    alanina_aminotransferiase = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    amilase = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    birrubina = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    birrubina_direita = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    colesterol_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    hdl_colesterol = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    ldl_colesterol = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    creatina = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    creatina_quinase = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    fosfatase_alcalina = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    gama_glutamil = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    glucose = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    lactato_desidrogenase = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    lactato = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    lipase = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    total_proteina = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    triglicerides = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    ureia = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    cloreto = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    potassio = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    sodio = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    globulinas = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    pcr = models.CharField(max_length=50, blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Exame Clinico'
        verbose_name_plural = 'Exames Clinicos'

    def __str__(self):
        return self.paciente.nome


class Fila(models.Model):
    data_inicio_tarv = models.DateTimeField(null=True, blank=True)
    data_levantamento = models.DateTimeField(null=True, blank=True)
    regime = models.CharField(max_length=100, null=True, blank=True)
    formulacao = models.CharField(max_length=100, blank=True, null=True)
    quantidade = models.IntegerField(null=True, blank=True)
    dosagem = models.CharField(max_length=100, null=True, blank=True)
    data_proximo_levantamento = models.DateTimeField(null=True, blank=True)
    lev_capmo_acomodacao = models.CharField(
        max_length=100, blank=True, null=True)
    numero_campo = models.IntegerField(null=True, blank=True)
    modo_dispensa = models.CharField(max_length=100, blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.paciente.nome


class Filt(models.Model):
    data_levantamento = models.DateTimeField(auto_now=False)
    regime_tpt = models.CharField(max_length=100)
    tipo_dispensa = models.CharField(max_length=100)
    seguimento_tratamento = models.CharField(
        max_length=100, blank=True, null=True)
    data_proximo_levantamento = models.DateTimeField(auto_now=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.regime_tpt
