{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "21e09b32-69b0-448e-b75a-1fbcb52d8e67",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'predictor'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mpredictor\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m show_predict_page\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mExplorer\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m show_explore_page\n\u001b[0;32m      6\u001b[0m page \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39msidebar\u001b[38;5;241m.\u001b[39mselectbox(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mExplore Or Predict\u001b[39m\u001b[38;5;124m\"\u001b[39m, (\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPredict\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mExplore\u001b[39m\u001b[38;5;124m\"\u001b[39m))\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'predictor'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from predictor import show_predict_page\n",
    "from Explorer import show_explore_page\n",
    "\n",
    "\n",
    "page = st.sidebar.selectbox(\"Explore Or Predict\", (\"Predict\", \"Explore\"))\n",
    "\n",
    "if page == \"Predict\":\n",
    "    show_predict_page()\n",
    "else:\n",
    "    show_explore_page()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25f1444e-026f-4724-b94b-8af2c772b034",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "838e9778-fda8-4e94-9a9d-05aaf469f2db",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
