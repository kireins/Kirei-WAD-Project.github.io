import streamlit as st
import sqlite3
import pandas as pd

# Fungsi untuk mengambil data dari SQLite
def get_data():
    conn = sqlite3.connect('tasks.db')
    tasks = pd.read_sql_query('SELECT * FROM tasks', conn)
    conn.close()
    return tasks

# Fungsi untuk menampilkan data tugas
def display_data():
    tasks = get_data()

    st.header("Daftar Tugas")
    st.dataframe(tasks)

    selected_id = st.text_input("Masukkan ID Tugas untuk Edit/Hapus")
    action = st.selectbox("Aksi", ["Lihat", "Edit", "Hapus"])

    if st.button("Lanjutkan"):
        if selected_id:
            st.session_state.selected_id = selected_id
            st.session_state.action = action
            if action == "Lihat":
                view_task(selected_id)
            elif action == "Edit":
                edit_task(selected_id)
            elif action == "Hapus":
                delete_task(selected_id)
                st.experimental_rerun()
        else:
            st.error("ID Tugas tidak boleh kosong.")

# Fungsi untuk melihat detail tugas
def view_task(task_id):
    tasks = get_data()
    task = tasks[tasks['id'] == task_id]
    if not task.empty:
        st.write(task)
    else:
        st.error("Tugas dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menambahkan tugas baru
def add_task():
    st.header("Tambah Tugas")
    id = st.text_input("ID Siswa")
    name = st.text_input("Nama Siswa")
    task = st.text_area("Tugas")
    status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])
    time = st.text_input("Waktu")
    location = st.text_input("Lokasi")

    if st.button("Tambah"):
        if id and name and task and time and location:  # Ensure required fields are not empty
            conn = sqlite3.connect('tasks.db')
            c = conn.cursor()
            c.execute('''
            INSERT INTO tasks (id, name, task, status, time, location)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (id, name, task, status, time, location))
            conn.commit()
            conn.close()
            st.success("Tugas berhasil ditambahkan!")
            st.experimental_rerun()
        else:
            st.error("Semua kolom harus diisi.")

# Fungsi untuk mengedit tugas
def edit_task(task_id):
    tasks = get_data()
    task = tasks[tasks['id'] == task_id]
    if not task.empty:
        task = task.iloc[0]
        name = st.text_input("Nama Siswa", task['name'])
        task_text = st.text_area("Tugas", task['task'])
        status = st.selectbox("Status", ["Pending", "In Progress", "Completed"], index=["Pending", "In Progress", "Completed"].index(task['status']))
        time = st.text_input("Waktu", task['time'])
        location = st.text_input("Lokasi", task['location'])

        if st.button("Simpan"):
            if name and task_text and time and location:  # Ensure required fields are not empty
                conn = sqlite3.connect('tasks.db')
                c = conn.cursor()
                c.execute('''
                UPDATE tasks
                SET name = ?, task = ?, status = ?, time = ?, location = ?
                WHERE id = ?
                ''', (name, task_text, status, time, location, task_id))
                conn.commit()
                conn.close()
                st.success("Tugas berhasil diperbarui!")
                st.experimental_rerun()
            else:
                st.error("Semua kolom harus diisi.")
    else:
        st.error("Tugas dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menghapus tugas
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''
    DELETE FROM tasks WHERE id = ?
    ''', (task_id,))
    conn.commit()
    conn.close()
    st.success("Tugas berhasil dihapus!")

st.sidebar.title("Panel Manajemen Tugas")
choice = st.sidebar.selectbox("Menu", ["Lihat Tugas", "Tambah Tugas"])

if choice == "Lihat Tugas":
    display_data()
elif choice == "Tambah Tugas":
    add_task()
