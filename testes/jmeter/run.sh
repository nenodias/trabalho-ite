#!/bin/sh
jmeter -n -t Trabalho-rest.jmx
jmeter -n -t Trabalho-rest-get.jmx
jmeter -n -t Trabalho-estático.jmx
jmeter -n -t Trabalho-dinamico.jmx
jmeter -n -t Trabalho-relatorio.jmx