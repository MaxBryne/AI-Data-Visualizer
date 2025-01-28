import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openai

# Streamlit App
st.title("Data Visualization and Analysis App")

# Upload Excel or CSV file
uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xlsx", "csv"])

if uploaded_file:
    # Read the file into a DataFrame
    try:
        # Load the data
        df = pd.read_excel(uploaded_file) if "xlsx" in uploaded_file.name else pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")

        # Display the DataFrame
        st.subheader("Data Preview")
        st.dataframe(df)

        # Plot Options
        st.subheader("Select Plot Type")
        plot_type = st.selectbox(
            "Choose a plot type",
            ["Scatter Plot", "Line Plot", "Bar Plot", "Histogram", "Heatmap"]
        )

        # Column Selection for Plots
        if plot_type != "Heatmap":
            x_axis = st.selectbox("Select X-axis", df.columns)
            y_axis = st.selectbox("Select Y-axis", df.columns)

        # Generate Plot
        if st.button("Generate Plot"):
            plt.figure(figsize=(10, 6))

            try:
                if plot_type == "Scatter Plot":
                    sns.scatterplot(data=df, x=x_axis, y=y_axis)
                    plt.title(f"Scatter Plot of {x_axis} vs {y_axis}")

                elif plot_type == "Line Plot":
                    sns.lineplot(data=df, x=x_axis, y=y_axis)
                    plt.title(f"Line Plot of {x_axis} vs {y_axis}")

                elif plot_type == "Bar Plot":
                    sns.barplot(data=df, x=x_axis, y=y_axis)
                    plt.title(f"Bar Plot of {x_axis} vs {y_axis}")

                elif plot_type == "Histogram":
                    sns.histplot(data=df[x_axis], bins=20, kde=True)
                    plt.title(f"Histogram of {x_axis}")

                elif plot_type == "Heatmap":
                    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
                    plt.title("Heatmap of Correlation Matrix")

                st.pyplot(plt)
            except Exception as e:
                st.error(f"Error generating plot: {e}")

    except Exception as e:
        st.error(f"Error processing the file: {e}")

st.write("Built by Mayukh using Streamlit.")
