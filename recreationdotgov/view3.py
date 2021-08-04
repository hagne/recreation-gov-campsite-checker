from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.tab import MDTabs
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.textfield import MDTextField
from kivy.uix.widget import Widget
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
# KV = '''
# MDBoxLayout:
#     orientation: "vertical"

#     MDToolbar:
#         title: "Example Tabs"

#     MDTabs:
#         id: tabs
#         on_tab_switch: app.on_tab_switch(*args)


# <Tab>

#     MDLabel:
#         id: label
#         # text: "Tab 0"
#         halign: "center"
# '''


# class Tab(MDBoxLayout, MDTabsBase):
#     '''Class implementing content for a tab.'''
class Tab(MDGridLayout,MDTabsBase):
    '''Class implementing content for a tab.'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = 'vertical'
        # self.padding = 2
        self.padding = "5dp"
        # self.size = self.parent.size
        # self.adaptive_size = True 
        self.cols = 3
        self.rows = 3
   
class StandardButton(MDRectangleFlatButton):
    """my standard buttons"""
    def  __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 5
    
class StandardDateField(MDTextField):
    """my standard textfield"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = 'mm/dd/yyyy'
   
class StandardLabel(MDLabel):
    """my standard label"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None,None)
        self.height = 35
    
    
class SaveButton(StandardButton):
    """sdf"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'save'
        # self.bind('on_press', self.on_save)
    
    def on_press(self, **kwargs):
        print(self.parent.size)

class SearchButton(StandardButton):
    """sdf"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'search'
        self.padding = 5
        # self.bind('on_press', self.on_save)
    
    def on_press(self, **kwargs):
        print(self.parent.size)

class SelectDateButton(StandardButton):
    """sdf"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'start Date'
        # self.padding = 10
        
    def on_press(self, **kwargs):
        date_dialog = MDDatePicker(lambda x: x)
        # date_dialog = MDDatePicker(lambda x: x, mode = 'range')
        self.date_dialog = date_dialog
        # self.date_dialog.padding = 10
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
        
        
    def on_save(self):
        print(self.parent.size)
        
        pass
    
    def on_cancel(self):
        pass
    
class StartDateContainer(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.adaptive_width = True
        self.orientation = 'horizontal'
        self.padding = 2
        self.add_widget(SelectDateButton())
        self.add_widget(SelectDateButton())
        self.start_date_text = StandardTextField()
        self.start_date_text.hint_text = 'mm/dd/yyyy'
        self.add_widget(self.start_date_text)
        
    


class Example(MDApp):
    def build(self):
        # box around evertying
        box_global = MDBoxLayout()
        box_global.orientation = 'vertical'
        # add the toolbar
        box_global.add_widget(MDToolbar(title = 'buba'))
        
        # add the tabs
        tabs = MDTabs()
        box_global.add_widget(tabs)
        
        # The search tab
        # tab = MDTabsBase()
        tab = Tab()
        # tab.size_hint = (None,None)
        tab.size = box_global.size
        tab.spacing = 10
        tab.text = 'search'
        tabs.add_widget(tab)
                
        
        tab.add_widget(StandardLabel(text = 'Check-in'))
        tab.add_widget(SelectDateButton())
        tab.add_widget(StandardDateField())
        
        tab.add_widget(StandardLabel(text = 'Check-out'))
        tab.add_widget(SelectDateButton())
        tab.add_widget(StandardDateField())
        
        tab.add_widget(SaveButton())
        tab.add_widget(SearchButton())
        
        # tab.padding_top = 3
        # tab.add_widget(Widget())
        
        return box_global
    
    #     def build(self):
    #     # box around evertying
    #     box_global = MDBoxLayout()
    #     box_global.orientation = 'vertical'
    #     # add the toolbar
    #     box_global.add_widget(MDToolbar(title = 'buba'))
        
    #     # add the tabs
    #     tabs = MDTabs()
    #     box_global.add_widget(tabs)
        
    #     # The search tab
    #     tab = MDTabsBase()
    #     tab.text = 'search'
    #     tabs.add_widget(tab)
        
    #     box = MDBoxLayout()
    #     tab.add_widget(box)
    #     box.orientation = 'vertical'
        
    #     # button = MDFlatButton()
    #     box.add_widget(StartDateContainer())
    #     box.add_widget(SaveButton())
        
    #     return box_global
    
    
    
        # return Builder.load_string(KV)

    # def on_start(self):
    #     for i in range(6):
    #         tab = Tab()
    #         tab.text = f"Tab {i}"
    #         self.root.ids.tabs.add_widget(tab)
    #         # self.root.ids.tabs.add_widget(Tab(title=f"Tab {i}"))


    # def on_tab_switch(
    #     self, instance_tabs, instance_tab, instance_tab_label, tab_text
    # ):
    #     '''Called when switching tabs.

    #     :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
    #     :param instance_tab: <__main__.Tab object>;
    #     :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
    #     :param tab_text: text or name icon of tab;
    #     '''
    #     pass
    #     # print( instance_tab.ids.label.text)
    #     # instance_tab.ids.label.text = tab_text
    #     # print(type(instance_tab.ids.label))


ki = Example().run()