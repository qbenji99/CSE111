from names import make_full_name, extract_given_name,     extract_family_name
import pytest


def test_make_full_name():
  #
  assert make_full_name("Maryna","Kryvoruchenko") == "Kryvoruchenko; Maryna"
  assert make_full_name("Troy", "Romriell-Mcgee") == "Romriell-Mcgee; Troy"
  assert make_full_name("Ben","Quiñones") == "Quiñones; Ben"
  
  #
   

def test_extract_family_name():
  #
  assert extract_family_name("Kryvoruchenko; Maryna") == "Kryvoruchenko"
  assert extract_family_name("Romriell-Mcgee; Troy") == "Romriell-Mcgee"
  assert extract_family_name("Quiñones; Ben") == "Quiñones"
  
  #   

def test_extract_given_name():
  #
  assert extract_given_name("Kryvoruchenko; Maryna") == "Maryna"
  assert extract_given_name("Romriell-Mcgee; Troy") == "Troy"
  assert extract_given_name("Quiñones; Ben") == "Ben"
  #

pytest.main(["-v", "--tb=line", "-rN", "10_team_activity5"])