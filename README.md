# �������� ������� � ������ �Asyncio�

� ���� ������� �� ����� ��������� �� API ���������� Start Wars � ��������� � ���� ������.<br>
������������ �� API ��������� �����: [SWAPI](https://swapi.dev/documentation#people). <br>
������ �������: `https://swapi.dev/api/people/1/` <br>
� ���������� ������� �������� ��������� � ID 1:
```
{
    "birth_year": "19 BBY",
    "eye_color": "Blue",
    "films": [
        "https://swapi.dev/api/films/1/",
        ...
    ],
    "gender": "Male",
    "hair_color": "Blond",
    "height": "172",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "mass": "77",
    "name": "Luke Skywalker",
    "skin_color": "Fair",
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-10T13:52:43.172000Z",
    "species": [
        "https://swapi.dev/api/species/1/"
    ],
    "starships": [
        "https://swapi.dev/api/starships/12/",
        ...
    ],
    "url": "https://swapi.dev/api/people/1/",
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/"
        ...
    ]
}
```
���������� ��������� c�������� ����:<br>
**id** - ID ��������� <br>
**birth_year** <br>
**eye_color** <br>
**films** - ������ � ���������� ������� ����� ������� <br>
**gender** <br>
**hair_color** <br>
**height** <br>
**homeworld** <br>
**mass** <br>
**name** <br>
**skin_color** <br>
**species** - ������ � ���������� ����� ����� ������� <br>
**starships** - ������ � ���������� �������� ����� ������� <br>
**vehicles** - ������ � ���������� ���������� ����� ������� <br>
������ �� ������� ��������� ���������� ��������� � ����� ���� ������. <br>
�������� �� ��� � �������� � ���� ������ ����������� ����������. <br>

����������� ������ �����: <br>
1) ������ �������� ���� ������ <br>
2) ������ �������� ������ �� API � ���� <br>

� ���� ������ ���� ��������� ��� ���������