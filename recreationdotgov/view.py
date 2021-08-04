import recreationdotgov.recreationlab as recreationlab

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
from kivymd.uix.textfield import MDTextField

# class Tab(MDBoxLayout, MDTabsBase):
#     '''Class implementing content for a tab.'''
# class Tab_Grid_not_used(MDGridLayout,MDTabsBase):
#     '''Class implementing content for a tab.'''
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         # self.orientation = 'vertical'
#         # self.padding = 2
#         self.padding = "5dp"
#         # self.size = self.parent.size
#         # self.adaptive_size = True 
#         self.cols = 3
#         self.rows = 3
        
class Tab(MDBoxLayout,MDTabsBase):
    '''Class implementing content for a tab.'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        # self.padding = 2
        self.padding = "5dp"
        self.pos_hint = {"center_x": .5, "top": 1}
        self.size_hint_x = .8
        self.size_hint_y = 1
        # self.size = self.parent.size
        # self.adaptive_size = True 
        # self.cols = 3
        # self.rows = 3

class SearchResult(MDTextField):
    """..."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # MDTextField:
        self.size_hint_x = .8
        self.size_hint_y = 1
        self.hint_text =  "search result"
        self.max_height =  "200dp"
        self.mode = "fill"
        # fill_color: 0, 0, 0, .4
        self.multiline = True
        self.pos_hint = {"center_x": .5, "top": 1}
        # self.pos_hint = {"center_x": .5, "center_y": .5}
        self.name = 'id_text_search_res'
        # self.text = "asdfasdfasdfasd asdf asdfasdfa asdfasdf asdf asdfasdf"
        

class StandardButton(MDRectangleFlatButton):
    """my standard buttons"""
    def  __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 5
    

class StandardInputField(MDTextField):
    """my standard textfield"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.hint_text = 'mm/dd/yyyy'
        
class InputCampgroundField(StandardInputField):
    """my standard textfield"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = 'Site ID'
        self.name = 'id_input_site'
        self.text = '232462'

class InputCampgroundFieldplus(StandardInputField):
    """my standard textfield"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = 'Site ID'
        # self.name = 'id_input_site'

class InputDateField(StandardInputField):
    """my standard textfield"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = 'mm/dd/yyyy'

class InputCheckIn(InputDateField):
    """my standard textfield"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name= 'id_input_checkin'
        self.text = '05/12/2021'

class InputNoOfNights(StandardInputField):
    """my standard textfield"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = '# of nights'
        self.name = 'id_input_no_of_nights'
        self.text = '1'
        
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
        # MDApp.get_running_app().root()
        # self.App.get_running_app()
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
        site_id = MDApp.get_running_app().get_widget_by_name('id_input_site').text
        checkin = MDApp.get_running_app().get_widget_by_name('id_input_checkin').text
        no_of_nights = MDApp.get_running_app().get_widget_by_name('id_input_no_of_nights').text
        print(f'{site_id}, {checkin}, {no_of_nights}')
        
        cg = recreationlab.Campground(site_id)
        cgc = recreationlab.CampgroundCollection([cg])
        resmessage = cgc.make_query(checkin_date=checkin, no_of_nights=int(no_of_nights))['res_msg']
        MDApp.get_running_app().get_widget_by_name('id_text_search_res').text = resmessage
        print(resmessage)

class SelectDateButton(StandardButton):
    """sdf"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'pick'
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
    
# class StartDateContainer(MDBoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         # self.adaptive_width = True
#         self.orientation = 'horizontal'
#         self.padding = 2
#         self.add_widget(SelectDateButton())
#         self.add_widget(SelectDateButton())
#         self.start_date_text = StandardField()
#         self.start_date_text.hint_text = 'mm/dd/yyyy'
#         self.add_widget(self.start_date_text)
        



class Example(MDApp):
    def build(self):
        # box around evertying
        box_global = MDBoxLayout()
        box_global.name = 'bababallsd'
        box_global.orientation = 'vertical'
        # add the toolbar
        box_global.add_widget(MDToolbar(title = 'buba'))
        
        # add the tabs
        tabs = MDTabs()
        box_global.add_widget(tabs)
        
        #### The search tab
        # tab = MDTabsBase()
        tab = Tab()
        tab.spacing = 10
        tab.text = 'search'
        tabs.add_widget(tab)
        
        #### # the search grid
        grid = MDGridLayout()
        grid.name = 'grid'
        tab.add_widget(grid)
        grid.cols = 3
        grid.rows = 4
        grid.spacing = 5
        
        grid.add_widget(InputCampgroundField())
        grid.add_widget(InputCampgroundFieldplus())
        grid.add_widget(InputCampgroundFieldplus())
        
        grid.add_widget(StandardLabel(text = 'Check-in'))
        grid.add_widget(SelectDateButton())
        grid.add_widget(InputCheckIn())
        
        grid.add_widget(StandardLabel(text = 'Check-out'))
        # grid.add_widget(SelectDateButton())
        grid.add_widget(InputNoOfNights())
        grid.add_widget(InputDateField())
        
        grid.add_widget(SearchButton())
        grid.add_widget(SaveButton())
        
        #### # search result
        tab.add_widget(SearchResult())
        # tab.padding_top = 3
        # tab.add_widget(Widget())
        
        #### collections tab
        tab = Tab()
        tab.spacing = 10
        tab.text = 'collections'
        tabs.add_widget(tab)
        
        #### workplan
        tab = Tab()
        tab.spacing = 10
        tab.text = 'collections'
        tabs.add_widget(tab)
        
        return box_global
    
    def get_widget_by_name(self, name):
        widgets = []
        for widget in self.root.walk():
            try:
                if widget.name == name:
                    widgets.append(widget)
                # print("{} -> {}".format(widget, widget.ids))
                # print("{} -> {}".format(widget, widget.name))
            except:
                pass
        if len(widgets) == 0:
            raise KeyError(f'No widgets named {name}')
        elif len(widgets) > 1:
            raise KeyError(f'More than 1 widget named {name}')
        
        return widgets[0]
            
            
    
    def bla(self):
        print('bla')
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