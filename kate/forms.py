from django import forms

class formA(forms.Form):
    qq=forms.CharField(label="式",widget=forms.Textarea(attrs={'cols': '50', 'rows': '1','style': 'font-size: 30px;'}))
class formB(forms.Form):
    class qq(forms.Form):
        QQ=(
        ("","元の進数を入力してください"),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'), 
        ('35', '35'),
        ('36', '36'))
        qq=forms.ChoiceField(label="変換前",choices=QQ)
    class ww(forms.Form):
        WW=(
        ("","変換先の進数を入力してください"),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'), 
        ('35', '35'),
        ('36', '36'))
        ww=forms.ChoiceField(label="変換後",choices=WW)
    class ee(forms.Form):
        ee=forms.CharField(label="変換する数",widget=forms.Textarea(attrs={'cols': '50', 'rows': '1','style': 'font-size: 30px;'}))
class formC(forms.Form):
    class qq(forms.Form):
        qq=forms.CharField(label="式①",widget=forms.Textarea(attrs={'cols': '50', 'rows': '1','style': 'font-size: 30px;'}))
    class ww(forms.Form):
        ww=forms.CharField(label="式②",widget=forms.Textarea(attrs={'cols': '50', 'rows': '1','style': 'font-size: 30px;'}))

