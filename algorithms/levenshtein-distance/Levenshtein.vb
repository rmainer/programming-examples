Imports System

Module Levenshtein

    Function Levenshtein(ByVal w1 As String, ByVal w2 As String) As UInteger
        w1 = w1.ToLower
        w2 = w2.ToLower
        Dim n1 As UInteger = w1.Length + 1
        Dim n2 As UInteger = w2.Length + 1
        Dim d(n1, n2) As UInteger

        For y As UInteger = 0 To n1 - 1
            For x As UInteger = 0 To n2 - 1
                d(y, x) = 0
            Next
        Next
        For y As UInteger = 1 To n1 - 1
            d(y, 0) = y
        Next
        For x As UInteger = 1 To n1 - 1
            d(0, x) = x
        Next

        For y As UInteger = 1 To n1 - 1
            For x As UInteger = 1 To n2 - 1
                If w1.Chars(y - 1) = w2.Chars(x - 1) Then
                    d(y, x) = d(y - 1, x - 1)
                Else
                    d(y, x) = Math.Min(d(y - 1, x - 1), Math.Min(d(y - 1, x), d(y, x - 1))) + 1
                End If
            Next
        Next

        Levenshtein = d(n1 - 1, n2 - 1)
    End Function


    Sub Main(args As String())
        Console.WriteLine(Levenshtein("Roman", "Ramo"))
    End Sub
End Module
