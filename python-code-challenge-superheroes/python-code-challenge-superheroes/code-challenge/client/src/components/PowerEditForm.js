import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";

function PowerEditForm() {
  const [{ data: power, errors, status }, setPower] = useState({
    data: null,
    errors: [], // Initialize errors to an empty array
    status: "pending",
  });
  const [description, setDescription] = useState("");
  const history = useNavigate();
  const { id } = useParams();

  useEffect(() => {
    fetch(`/powers/${id}`).then((r) => {
      if (r.ok) {
        r.json().then((power) => {
          setPower({ data: power, errors: [], status: "resolved" });
          setDescription(power.description);
        });
      } else {
        r.json().then((err) =>
          setPower({ data: null, errors: [err.error], status: "rejected" })
        );
      }
    });
  }, [id]);

  if (status === "pending") return <h1>Loading...</h1>;

  function handleSubmit(e) {
    e.preventDefault();
    fetch(`/powers/${power.id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        description,
      }),
    }).then((r) => {
      if (r.ok) {
        history.push(`/powers/${power.id}`);
      } else {
        r.json().then((err) =>
          setPower({ data: power, errors: err.errors, status: "rejected" })
        );
      }
    });
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Editing {power.name}</h2>
      <label htmlFor="description">Description:</label>
      <textarea
        id="description"
        name="description"
        rows="4"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      {errors && errors.length > 0  // Add a null check before accessing the length property
        ? errors.map((err) => (
            <p key={err} style={{ color: "red" }}>
              {err}
            </p>
          ))
        : null}
      <button type="submit">Update Power</button>
    </form>
  );
}

export default PowerEditForm;
