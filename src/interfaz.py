#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Fri Feb 18 22:29:38 2011

import wx
import csv
from algoritmos import algoritmos

class MyFrame(wx.Frame):

    def __init__(self, *args, **kwds):

        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.lbOrigen = wx.StaticText(self, -1, "Origen:", style=wx.ALIGN_CENTRE)
        self.cajaOrigen = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.lbDes = wx.StaticText(self, -1, "Destino:")
        self.cajaDestino = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.radioMin = wx.RadioButton(self, -1, "Minimizar")
        self.radioMax = wx.RadioButton(self, -1, "Maximizar")
        self.btAnch = wx.Button(self, -1, "Anchura")
        self.lbCoste = wx.StaticText(self, -1, "Coste: ")
        self.btProf = wx.Button(self, -1, "Profundidad")
        self.textCoste = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY|wx.TE_CENTRE)
        self.btProfAc = wx.Button(self, -1, "Profundidad acotada")
        self.lbElementos = wx.StaticText(self, -1, "Elementos generados: ")
        self.btProfIt = wx.Button(self, -1, "Profundidad iterativa")
        self.textElems = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY|wx.TE_CENTRE)
        self.btCosto = wx.Button(self, -1, "Costo uniforme")
        self.lbIns = wx.StaticText(self, -1, u"Tiempo de inserción medio:")
        self.btA = wx.Button(self, -1, "A*")
        self.textIns = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY|wx.TE_CENTRE)
        self.btTemple = wx.Button(self, -1, "Temple simulado")
        self.lbTiempo = wx.StaticText(self, -1, u"Tiempo de ejecución:")
        self.panel_1 = wx.Panel(self, -1)
        self.textTiempo = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY|wx.TE_CENTRE)
        self.lbCamino = wx.StaticText(self, -1, "Camino generado:")
        self.cajaCamino = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN|wx.CB_READONLY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBUTTON, self.setVal, self.radioMin)
        self.Bind(wx.EVT_RADIOBUTTON, self.setVal, self.radioMax)
        self.Bind(wx.EVT_BUTTON, self.anchura, self.btAnch)
        self.Bind(wx.EVT_BUTTON, self.prof, self.btProf)
        self.Bind(wx.EVT_BUTTON, self.porfAc, self.btProfAc)
        self.Bind(wx.EVT_BUTTON, self.ProfIt, self.btProfIt)
        self.Bind(wx.EVT_BUTTON, self.Costo, self.btCosto)
        self.Bind(wx.EVT_BUTTON, self.AStar, self.btA)
        self.Bind(wx.EVT_BUTTON, self.Temple, self.btTemple)
        # end wxGlade
        
        self.factor = 1.0
        self.nodos = MyFrame.__fillCombo(self)
        self.cajaOrigen.AppendItems(self.nodos)
        self.cajaDestino.AppendItems(self.nodos)
        self.cajaOrigen.SetValue(self.nodos[0])
        self.cajaDestino.SetValue(self.nodos[0])
        self.metodos = algoritmos()

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("P1 Inteligencia Artificial")
        self.SetSize((657, 594))
        self.lbOrigen.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.lbDes.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.radioMin.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.radioMax.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.btAnch.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.lbCoste.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.btProf.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.textCoste.SetMinSize((140, 27))
        self.btProfAc.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.lbElementos.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.btProfIt.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.textElems.SetMinSize((140, 27))
        self.btCosto.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.lbIns.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.btA.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.textIns.SetMinSize((140, 27))
        self.btTemple.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.lbTiempo.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.textTiempo.SetMinSize((140, 27))
        self.lbCamino.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(13, 1, 3, 3)
        grid_sizer_3 = wx.GridSizer(1, 2, 3, 3)
        grid_sizer_2_copy_9 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2_copy_8 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2_copy_7 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2_copy_6 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2_copy_5 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2_copy_4 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2_copy_3 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2_copy_2 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2_copy_1 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_2_copy = wx.GridSizer(1, 2, 0, 3)
        grid_sizer_2 = wx.GridSizer(1, 2, 0, 3)
        grid_sizer_2.Add(self.lbOrigen, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.cajaOrigen, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_2_copy.Add(self.lbDes, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2_copy.Add(self.cajaDestino, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(grid_sizer_2_copy, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_1.Add(self.radioMin, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2_copy_1.Add(self.radioMax, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(grid_sizer_2_copy_1, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_2.Add(self.btAnch, 0, wx.EXPAND, 0)
        grid_sizer_2_copy_2.Add(self.lbCoste, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(grid_sizer_2_copy_2, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_3.Add(self.btProf, 0, wx.EXPAND, 0)
        grid_sizer_2_copy_3.Add(self.textCoste, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(grid_sizer_2_copy_3, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_4.Add(self.btProfAc, 0, wx.EXPAND, 0)
        grid_sizer_2_copy_4.Add(self.lbElementos, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(grid_sizer_2_copy_4, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_5.Add(self.btProfIt, 0, wx.EXPAND, 0)
        grid_sizer_2_copy_5.Add(self.textElems, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(grid_sizer_2_copy_5, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_6.Add(self.btCosto, 0, wx.EXPAND, 0)
        grid_sizer_2_copy_6.Add(self.lbIns, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(grid_sizer_2_copy_6, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_7.Add(self.btA, 0, wx.EXPAND, 0)
        grid_sizer_2_copy_7.Add(self.textIns, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(grid_sizer_2_copy_7, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_8.Add(self.btTemple, 0, wx.EXPAND, 0)
        grid_sizer_2_copy_8.Add(self.lbTiempo, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(grid_sizer_2_copy_8, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_9.Add(self.panel_1, 1, wx.EXPAND, 0)
        grid_sizer_2_copy_9.Add(self.textTiempo, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(grid_sizer_2_copy_9, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.lbCamino, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_3.Add(self.cajaCamino, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        sizer_3.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        self.Layout()
        self.Centre()
        # end wxGlade
        
    def __fillCombo(self):
        l = []
        csvReader = csv.reader(open('nodes.csv', 'rb'))
        for row in csvReader:
            l.append(row[0])
        return l

    def setVal(self, event): # wxGlade: MyFrame.<event_handler>
        min = self.radioMin.GetValue()
        max = self.radioMax.GetValue()
        if min:
            self.factor =  1.0
        if max:
            self.factor = -1.0
        print self.factor
        event.Skip()

    def anchura(self, event): # wxGlade: MyFrame.<event_handler>
        g = self.metodos.genGraph()
        self.cajaCamino.Clear()
        sol = self.metodos.buscar(g, self.cajaOrigen.GetValue(), self.cajaDestino.GetValue(), 0, 0)
        self.textCoste.SetValue('%.2f' %(sol.valoracion))
        self.textElems.SetValue('%.0f' %(self.metodos.nelementos))
        self.textIns.SetValue('%.4e secs' %(self.metodos.tMedio))
        self.textTiempo.SetValue('%.3f secs' %(self.metodos.tiempo))
        self.cajaCamino.SetValue(sol.camino[0])
        self.cajaCamino.AppendItems(sol.camino)
        event.Skip()

    def prof(self, event): # wxGlade: MyFrame.<event_handler>
        g = self.metodos.genGraph()
        self.cajaCamino.Clear()
        sol = self.metodos.buscar(g, self.cajaOrigen.GetValue(), self.cajaDestino.GetValue(), 0, 1)
        self.textCoste.SetValue('%.2f' %(sol.valoracion))
        self.textElems.SetValue('%.0f' %(self.metodos.nelementos))
        self.textIns.SetValue('%.4e secs' %(self.metodos.tMedio))
        self.textTiempo.SetValue('%.3f secs' %(self.metodos.tiempo))
        self.cajaCamino.SetValue(sol.camino[0])
        self.cajaCamino.AppendItems(sol.camino)
        event.Skip()

    def porfAc(self, event): # wxGlade: MyFrame.<event_handler>
        g = self.metodos.genGraph()
        self.cajaCamino.Clear()
        sol = self.metodos.buscar(g, self.cajaOrigen.GetValue(), self.cajaDestino.GetValue(), 60, 2)
        self.textCoste.SetValue('%.2f' %(sol.valoracion))
        self.textElems.SetValue('%.0f' %(self.metodos.nelementos))
        self.textIns.SetValue('%.4e secs' %(self.metodos.tMedio))
        self.textTiempo.SetValue('%.3f secs' %(self.metodos.tiempo))
        self.cajaCamino.SetValue(sol.camino[0])
        self.cajaCamino.AppendItems(sol.camino)
        event.Skip()

    def ProfIt(self, event): # wxGlade: MyFrame.<event_handler>
        g = self.metodos.genGraph()
        self.cajaCamino.Clear()
        sol = self.metodos.buscar(g, self.cajaOrigen.GetValue(), self.cajaDestino.GetValue(), 1, 3)
        self.textCoste.SetValue('%.2f' %(sol.valoracion))
        self.textElems.SetValue('%.0f' %(self.metodos.nelementos))
        self.textIns.SetValue('%.4e secs' %(self.metodos.tMedio))
        self.textTiempo.SetValue('%.3f secs' %(self.metodos.tiempo))
        self.cajaCamino.SetValue(sol.camino[0])
        self.cajaCamino.AppendItems(sol.camino)
        event.Skip()

    def Costo(self, event): # wxGlade: MyFrame.<event_handler>
        g = self.metodos.genGraph()
        self.cajaCamino.Clear()
        sol = self.metodos.buscar(g, self.cajaOrigen.GetValue(), self.cajaDestino.GetValue(), 1, self.factor * 4)
        self.textCoste.SetValue('%.2f' %(sol.valoracion))
        self.textElems.SetValue('%.0f' %(self.metodos.nelementos))
        self.textIns.SetValue('%.4e secs' %(self.metodos.tMedio))
        self.textTiempo.SetValue('%.3f secs' %(self.metodos.tiempo))
        self.cajaCamino.SetValue(sol.camino[0])
        self.cajaCamino.AppendItems(sol.camino)
        event.Skip()

    def AStar(self, event): # wxGlade: MyFrame.<event_handler>
        g = self.metodos.genGraph()
        self.cajaCamino.Clear()
        sol = self.metodos.buscar(g, self.cajaOrigen.GetValue(), self.cajaDestino.GetValue(), 1, self.factor * 5)
        self.textCoste.SetValue('%.2f' %(sol.valoracion))
        self.textElems.SetValue('%.0f' %(self.metodos.nelementos))
        self.textIns.SetValue('%.4e secs' %(self.metodos.tMedio))
        self.textTiempo.SetValue('%.3f secs' %(self.metodos.tiempo))
        self.cajaCamino.SetValue(sol.camino[0])
        self.cajaCamino.AppendItems(sol.camino)
        event.Skip()
    def Temple(self, event): # wxGlade: MyFrame.<event_handler>
        g = self.metodos.genGraph()
        self.cajaCamino.Clear()
        self.btAnch.Disable()
        self.btProf.Disable()
        self.btProfAc.Disable()
        self.btProfIt.Disable()
        self.btCosto.Disable()
        self.btA.Disable()
        self.btTemple.Disable()
        sol, t = self.metodos.templeSimulado(g, self.cajaOrigen.GetValue(), self.cajaDestino.GetValue())
        self.btAnch.Enable()
        self.btProf.Enable()
        self.btProfAc.Enable()
        self.btProfIt.Enable()
        self.btCosto.Enable()
        self.btA.Enable()
        self.btTemple.Enable()
        print sol.camino
        print "Valoración: %.2f" %(sol.valoracion)
        print "Tiempo de ejecución: %.3f" %(t)
        print '--------------------------------------------------------'
        self.textCoste.SetValue('%.2f' %(sol.valoracion))
        self.textTiempo.SetValue('%.3f secs' %(t))
        self.cajaCamino.SetValue(sol.camino[0])
        self.cajaCamino.AppendItems(sol.camino)
        event.Skip()
# end of class MyFrame


class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        mainFrame = MyFrame(None, -1, "")
        self.SetTopWindow(mainFrame)
        mainFrame.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
