program levenshtein;
uses math;

function levenshtein(w1: string; w2: string): integer;
var
	d : array of array of integer;
	n1, n2, x, y: integer;
begin
	w1 := lowercase(w1);
	w2 := lowercase(w2);
	n1 := length(w1) + 1;
	n2 := length(w2) + 1;
	
	setlength(d, n1);
	for y := 1 to n1 do
	begin
		setlength(d[y], n2);
		for x := 1 to n2 do
		begin
			d[y][x] := 0;
		end;
	end;
	for y := 2 to n1 do
	begin
		d[y][1] := y;
	end;	
	for x := 2 to n2 do
	begin
		d[1][x] := x;
	end;

	for y := 2 to n1 do
	begin
		for x := 2 to n2 do
		begin
			if w1[y-1] = w2[x-1] then d[y][x] := d[y-1][x-1]
			else d[y][x] := min(d[y-1][x-1], min(d[y-1][x], d[y][x-1])) + 1;
		end;
	end;

	levenshtein := d[n1][n2];
end;

begin
	writeln(levenshtein('Roman', 'Ramo'));
end.