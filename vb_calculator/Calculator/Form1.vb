Public Class Form1
	Dim addres As Integer
	Dim subres As Integer
	Dim finalres As Integer
	Private Sub Num9_Click(sender As Object, e As EventArgs) Handles Num9.Click
		CalcScreen.Text = CalcScreen.Text + "9"
	End Sub

	Private Sub Num1_Click(sender As Object, e As EventArgs) Handles Num1.Click
		CalcScreen.Text = CalcScreen.Text + "1"
	End Sub

	Private Sub Num2_Click(sender As Object, e As EventArgs) Handles Num2.Click
		CalcScreen.Text = CalcScreen.Text + "2"
	End Sub

	Private Sub Num3_Click(sender As Object, e As EventArgs) Handles Num3.Click
		CalcScreen.Text = CalcScreen.Text + "3"
	End Sub

	Private Sub Num4_Click(sender As Object, e As EventArgs) Handles Num4.Click
		CalcScreen.Text = CalcScreen.Text + "4"
	End Sub

	Private Sub Num5_Click(sender As Object, e As EventArgs) Handles Num5.Click
		CalcScreen.Text = CalcScreen.Text + "5"
	End Sub

	Private Sub Num6_Click(sender As Object, e As EventArgs) Handles Num6.Click
		CalcScreen.Text = CalcScreen.Text + "6"
	End Sub

	Private Sub Num7_Click(sender As Object, e As EventArgs) Handles Num7.Click
		CalcScreen.Text = CalcScreen.Text + "7"
	End Sub

	Private Sub Num8_Click(sender As Object, e As EventArgs) Handles Num8.Click
		CalcScreen.Text = CalcScreen.Text + "8"
	End Sub

	Private Sub Clear_Click(sender As Object, e As EventArgs) Handles Clear.Click
		CalcScreen.Text = ""
		addres = 0
	End Sub

	Private Sub ButtPlus_Click(sender As Object, e As EventArgs) Handles ButtPlus.Click
		addres = addres + Val(CalcScreen.Text)
		CalcScreen.Clear()
	End Sub

	Private Sub ButtMin_Click(sender As Object, e As EventArgs) Handles ButtMin.Click
		subres = subres - Val(CalcScreen.Text)
		CalcScreen.Clear()
	End Sub

	Private Sub ButtEq_Click(sender As Object, e As EventArgs) Handles ButtEq.Click
		finalres = addres + Val(CalcScreen.Text)
		CalcScreen.Text = finalres
		addres = 0
	End Sub

End Class
