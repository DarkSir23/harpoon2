from bootstrap_modal_forms.forms import BSModalModelForm
from django.forms import ValidationError
from .models import DownloadFolder, Manager, Downloader
import os

class DLFolderModalForm(BSModalModelForm):
    class Meta:
        model = DownloadFolder
        exclude = ['pk']

    def clean_folder(self):
        data = self.cleaned_data['folder']
        if os.path.exists(data) and os.path.isdir(data):
            return data
        elif os.path.exists(data) and os.path.isfile(data):
            self.add_error('folder', ValidationError('Path exists, but is a file.  Please only enter a folder.'))
        else:
            try:
                os.makedirs(data)
            except PermissionError:

                self.add_error('folder', ValidationError('Folder does not exist and could not be created.  Please check permissions.'))
            except NotADirectoryError:
                self.add_error('folder', ValidationError('Invalid directory.  Check the path and try again.'))
        return data


class ManagerModalForm(BSModalModelForm):
    class Meta:
        model = Manager
        exclude = ['pk']

class DownloaderModalForm(BSModalModelForm):

    def __init__(self, *args, **kwargs):
        super(SchoolModelForm, self).__init__(*args, **kwargs)
        if hasattr(self, 'instance'):
            options = self.instance.options
            for item in options.keys():
                self.fields[f'opt_{item}'] = forms.CharField(required=False, label=f'Personnel ({group})', widget=forms.Textarea)
                self.fields[f'opt_{item}'].initial = PersonList(self.instance.personnel[group]).to_string()

    class Meta:
        model = Downloader
        exclude = ['pk']

