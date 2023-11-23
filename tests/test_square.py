import pytest
import source.shapes as shapes

@pytest.mark.parametrize("side, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_areas(side, expected_area):
    assert shapes.Square(side).area() == expected_area


@pytest.mark.parametrize("side, expected_perimeter", [(5, 20), (4, 16), (9, 36)])
def test_multiple_square_perimeters(side, expected_perimeter):
    assert shapes.Square(side).perimeter() == expected_perimeter