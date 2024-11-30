import unittest
from datetime import datetime
from NoteManager import Note, NoteManager


class TestNote(unittest.TestCase):
    def test_note_creation(self):
        note = Note('Здати лабораторні', '24-09-2027' )
        self.assertEqual(note.content, 'Здати лабораторні')
        self.assertEqual(note.event_date, datetime.strptime('24-09-2027', '%d-%m-%Y'))

    def test_note_lt(self):
        note1 = Note('Нотатка 1', '24-09-2024')
        note2 = Note('Нотатка 2', '25-09-2024')
        self.assertTrue(note1 < note2)

    def test_note_eq(self):
        note1 = Note('Нотатка1', '24-09-2024')
        note2 = Note('Нотатка1', '24-09-2024')
        note3 = Note('Інша нотатка3', '25-09-2024')
        self.assertEqual(note1, note2)
        self.assertNotEqual(note1, note3)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            Note('Нотатка21', '2025-09-24')  # Неправильний формат дати


class TestNoteManager(unittest.TestCase):
    def setUp(self):
        self.note_manager = NoteManager()

    def test_add_note(self):
        self.note_manager.add_note("Перша нотатка", "24-09-2024")
        self.assertEqual(len(self.note_manager.notes_queue), 1)
        self.assertEqual(self.note_manager.notes_queue[0].content, "Перша нотатка")

    def test_add_duplicate_note(self):
        self.note_manager.add_note("Нотатка", "24-09-2024")
        self.note_manager.add_note("Нотатка", "24-09-2024")
        self.assertEqual(len(self.note_manager.notes_queue), 1)

    def test_get_notes_by_date(self):
        self.note_manager.add_note("Нотатка 1", "24-09-2024")
        self.note_manager.add_note("Нотатка 2", "25-09-2024")
        notes = self.note_manager.get_notes_by_date("24-09-2024")
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].content, "Нотатка 1")

    def test_delete_note_by_index(self):
        self.note_manager.add_note("Нотатка для видалення", "24-09-2024")
        self.note_manager.delete_note_by_index("24-09-2024", 0)
        self.assertEqual(len(self.note_manager.notes_queue), 0)

    def test_edit_note_by_index(self):
        self.note_manager.add_note("Стара нотатка", "24-09-2024")
        self.note_manager.edit_note_by_index("24-09-2024", 0, "Нова нотатка")
        self.assertEqual(self.note_manager.notes_queue[0].content, "Нова нотатка")
        
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)


if __name__ == '__main__':
    unittest.main()
